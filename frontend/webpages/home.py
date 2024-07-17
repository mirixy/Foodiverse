import streamlit as st
import openfoodfacts
from backend.modules.data_processor import product, filter_nutriments,  nutriments, nutriments_dataframe, nutrigrade, nutriscore, get_multiple_products
from backend.modules.product_filters import nutriments_filters

#Functions
def get_product_nutriments(product: dict) -> dict:
    """Return nutriments data as dictionary."""
    nutriments_dict = nutriments(product)


st.title("FoodFacts")
# Getting API response
api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0", timeout=100)
#code = "3017620422003"
#resp_text = api.product.text_search('Nutella')
#resp_code = api.product.get(code)
    

def search_product():
    if 'clear_inputs' not in st.session_state:
        st.session_state.clear_inputs = False

    if st.session_state.clear_inputs:
        st.session_state.product_input = ''
        st.session_state.clear_inputs = False

    col1, col2 = st.columns([2,1])
    with col1:
        products = st.text_input("Enter product name", key="product_input")
    with col2:
        if st.button("Search"):
            perform_search()

    if 'search_performed' in st.session_state and st.session_state.search_performed:
        display_product_selection()

def perform_search():
    products = st.session_state.product_input
    if products:
        resp_text = api.product.text_search(products)
        multiple_products = get_multiple_products(resp_text)
        st.session_state.products = multiple_products
        st.session_state.search_performed = True
        st.session_state.clear_inputs = False

def display_product_selection():
    if 'products' in st.session_state and st.session_state.products:
        product_options = [f"{p['product_name']} (Barcode: {p['code']})" for p in st.session_state.products]
        selected_product = st.selectbox("Select a product", product_options)
        
        if selected_product:
            display_product_details(selected_product)

def display_product_details(selected_product):
    barcode = selected_product.split("(Barcode: ")[1].strip(")")
    resp_code = api.product.get(barcode)
    single_product = product(resp_code)
    single_product_copy_filtered = filter_nutriments(single_product, nutriments_filters)
    
    st.subheader("Current Nutrient Data:")
    col1, col2 = st.columns([1.5, 2])
    with col1:
        grade = nutrigrade(single_product_copy_filtered)
        colored_grade = color_nutrigrade(grade)
        st.markdown(f"### Nutrigrade: {colored_grade}", unsafe_allow_html=True)
    with col2:
        st.subheader("Nutrients in 100g:")
        st.write(nutriments_dataframe(single_product_copy_filtered))

        
          
def color_nutrigrade(grade):
    grade = grade.upper()
    if grade in ['A', 'B']:
        return f"<span style='color: green;'>{grade}</span>"
    elif grade in ['C']:
        return f"<span style='color: yellow;'>{grade}</span>"
    elif grade in ['D', 'E']:
        return f"<span style='color: red;'>{grade}</span>"
    else:
        return "Unknown"      


def display_data():
    if 'products' in st.session_state and st.session_state.products:
        product_options = [f"{p['product_name']} (Barcode: {p['code']})" for p in st.session_state.products]
        selected_product = st.selectbox("Select a product", product_options)
        
        if selected_product:
            barcode = selected_product.split("(Barcode: ")[1].strip(")")
            resp_code = api.product.get(barcode)
            single_product = product(resp_code)
            single_product_copy_filtered = filter_nutriments(single_product, nutriments_filters)
            
            st.subheader("Current Nutrient Data:")
            col1, col2 = st.columns([1.5, 2])
            with col1:
                grade = nutrigrade(single_product_copy_filtered)
                colored_grade = color_nutrigrade(grade)
                st.markdown(f"### Nutrigrade: {colored_grade}", unsafe_allow_html=True)
            with col2:
                st.subheader("Nutrients in 100g:")
                st.write(nutriments_dataframe(single_product_copy_filtered))
    else:
        st.write("No products found")





    
    
       

search_product()
    

