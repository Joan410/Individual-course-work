import streamlit as st
import datetime
import qrcode
import io
from PIL import Image
import random
import string
import base64

# Set page config
st.set_page_config(page_title="Victoria University Exhibition System", 
                   layout="centered",
                   initial_sidebar_state="collapsed")

# Custom CSS for elegant and modern design inspired by CustomTkinter
st.markdown("""
<style>
    /* Main container styling - dark mode inspired */
    .main .block-container {
        padding-top: 0;
        padding-bottom: 0;
        max-width: 850px;
    }
    
    /* Global page styling */
    .stApp {
        background-color: #1e1e2e;
    }
    
    /* Header styling */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        background: #2a2a3c;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* Form containers */
    .form-container {
        background: #2a2a3c;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    
    /* Input fields styling */
    .stTextInput > div > div {
        background-color: #3b3b4f;
        color: white;
        border-radius: 10px;
        border: 1px solid #4a4a5a;
    }
    
    .stTextInput input {
        color: white;
    }
    
    .stTextInput input::placeholder {
        color: #a0a0a0;
    }
    
    .stSelectbox > div > div {
        background-color: #3b3b4f;
        color: white;
        border-radius: 10px;
        border: 1px solid #4a4a5a;
    }
    
    /* Button styling */
    .stButton button {
        border-radius: 10px;
        padding: 10px 15px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    
    .login-button button {
        background-color: #0074cc;
        color: white;
    }
    
    .register-button button {
        background-color: #0074cc;
        color: white;
    }
    
    .proceed-button button {
        background-color: #0074cc;
        color: white;
    }
    
    .back-button button {
        background-color: transparent;
        color: #0074cc;
        border: 2px solid #0074cc;
    }
    
    .confirm-button button {
        background-color: #0074cc;
        color: white;
    }
    
    .home-button button {
        background-color: transparent;
        color: #0074cc;
        border: 2px solid #0074cc;
    }
    
    .print-button button {
        background-color: #0074cc;
        color: white;
    }
    
    .logout-button button {
        background-color: transparent;
        color: #FF0000;
        border: 2px solid #FF0000;
    }
    
    /* Ticket selection styling - enhanced colors */
    .seating-section {
        background-color: #3b3b4f;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
        cursor: pointer;
    }
    
    .seating-section:hover {
        transform: translateY(-5px);
    }
    
    .front-section {
        background-color: #ffecd2;
        color: #333;
    }
    
    .middle-section-blue {
        background-color: #d1eaff;
        color: #333;
    }
    
    .middle-section-green {
        background-color: green;
        color: #333;
    }
    
    .balcony-section {
        background-color: #e6e6e6;
        color: #333;
    }
    
    /* Ticket confirmation styling */
    .ticket-confirmation {
        background-color: #3b3b4f;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        color: white;
    }
    
    /* Success message styling */
    .success-message {
        color: #28a745;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin: 30px 0;
    }
    
    .success-icon {
        font-size: 60px;
        color: #28a745;
        text-align: center;
    }
    
    /* VU logo styling */
    .vu-logo {
        width: 60px;
        height: 60px;
        background-color: #ff3333;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto 10px auto;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .vu-logo-text {
        color: white;
        font-weight: bold;
        font-size: 24px;
    }
    
    /* Layout adjustments */
    .row {
        display: flex;
        gap: 20px;
    }
    
    .col {
        flex: 1;
    }
    
    /* Event card styling */
    .event-card {
        background-color: #3b3b4f;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
        cursor: pointer;
        color: white;
    }
    
    .event-card:hover {
        transform: translateY(-5px);
    }
    
    .keynote-card {
        background-color: #d1eaff;
        color: #333;
    }
    
    .workshop-card {
        background-color: #d1ffbd;
        color: #333;
    }
    
    .view-seats-button {
        color: #0074cc;
        font-weight: bold;
        margin-top: 10px;
    }
    
    /* Selection indicator */
    .selection-indicator {
        color: #ff9500;
        font-weight: bold;
        margin-top: 15px;
        font-size: 16px;
    }
    
    /* Title styling */
    .red-title {
        color: #ff3333;
    }
    
    .blue-title {
        color: #0a4275;
    }
    
    /* Text colors */
    h1, h2, h3, p, li, span {
        color: white;
    }
    
    /* White boxed content */
    .white-box {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        color: #333;
    }
    
    /* QR code and barcode styling */
    .qr-code {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        width: fit-content;
        margin: 15px auto;
    }
    
    .barcode {
        background-color: white;
        border-radius: 5px;
        padding: 10px;
        width: fit-content;
        margin: 10px auto;
        color: #333;
        font-family: monospace;
        font-size: 14px;
    }
    
    /* Card styling */
    .card {
        background-color: #2a2a3c;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    
    /* Adjust input fields */
    div[data-baseweb="input"] {
        width: 100%;
    }
    
    div[data-baseweb="select"] {
        width: 100%;
    }
    
    /* Labels for inputs */
    label {
        color: #d1d1d1;
        font-weight: 600;
        margin-bottom: 8px;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# Generate University logo
def get_vu_logo():
    logo_html = """
    <div style="text-align: center; margin-bottom: 10px;">
        <div class="vu-logo">
            <span class="vu-logo-text">VU</span>
        </div>
    </div>
    """
    return logo_html

# Generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to bytes
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Generate a simple barcode (simulated as text for now)
def generate_barcode():
    return ''.join(random.choices(string.digits, k=20))

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': '',
        'email': '',
        'phone': '',
        'affiliation': ''
    }
if 'selected_event' not in st.session_state:
    st.session_state.selected_event = None
if 'selected_seat' not in st.session_state:
    st.session_state.selected_seat = None

# Functions to change pages
def go_to_events():
    st.session_state.page = 'events'

def go_to_seats():
    if not st.session_state.selected_event:
        st.error("Please select an event before proceeding.")
        return
    st.session_state.page = 'seats'

def go_to_confirmation():
    if not st.session_state.selected_event or not st.session_state.selected_seat:
        st.error("Please select both an event and a seat before confirming.")
        if not st.session_state.selected_event:
            st.session_state.page = 'events'
        elif not st.session_state.selected_seat:
            st.session_state.page = 'seats'
        return
    st.session_state.page = 'confirmation'

def go_to_success():
    st.session_state.page = 'success'

def go_to_login():
    st.session_state.page = 'login'

def select_event(event):
    st.session_state.selected_event = event
    go_to_seats()

def select_seat(seat, price):
    st.session_state.selected_seat = {
        'seat': seat,
        'price': price
    }

# Login page
if st.session_state.page == 'login':
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 4])
    
    with col1:
        # st.markdown(f"""
        # # <div style="text-align: center;">
        # #     {get_vu_logo()}
        # #     <h1><span class="red-title">VICTORIA</span> <span class="blue-title">UNIVERSITY</span></h1>
        # #     <h2 class="blue-title">EXHIBITION SYSTEM</h2>
        # # </div>
        # # """, unsafe_allow_html=True)
        st.subheader("VICTORIA UNIVERSITY")
        st.text("EXHIBITION SYSTEM")
        
        st.markdown('<label>Full Name</label>', unsafe_allow_html=True)
        name = st.text_input("", placeholder="Enter name...", key="name_input", label_visibility="collapsed")
        
        st.markdown('<label>Email</label>', unsafe_allow_html=True)
        email = st.text_input("", placeholder="Enter email...", key="email_input", label_visibility="collapsed")
        
        st.markdown('<label>Phone</label>', unsafe_allow_html=True)
        phone = st.text_input("", placeholder="Enter phone number...", key="phone_input", label_visibility="collapsed")
        
        st.markdown('<label>Affiliation</label>', unsafe_allow_html=True)
        affiliation = st.selectbox("", ["Select one", "Student", "Faculty", "Staff", "Guest"], index=0, label_visibility="collapsed")
        
        col1_1, col1_2 = st.columns(2)
        
        with col1_1:
            st.markdown('<div class="login-button">', unsafe_allow_html=True)
            login_btn = st.button("Login →")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col1_2:
            st.markdown('<div class="register-button">', unsafe_allow_html=True)
            register_btn = st.button("Register 👤")
            st.markdown('</div>', unsafe_allow_html=True)
            
        if login_btn or register_btn:
            if not name or not email or not phone or affiliation == "Select one":
                st.error("Please fill in all fields")
            else:
                st.session_state.user_data['name'] = name
                st.session_state.user_data['email'] = email
                st.session_state.user_data['phone'] = phone
                st.session_state.user_data['affiliation'] = affiliation
                go_to_events()
    
    with col2:
        # st.sidebar.image("https://images.pexels.com/photos/207691/pexels-photo-207691.jpeg", width=100, use_container_width=True)
        st.image("https://images.pexels.com/photos/207691/pexels-photo-207691.jpeg", width=300, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Events page
elif st.session_state.page == 'events':
    col1, col2, col3 = st.columns([2,2,1])
    with col2:
        st.image("https://pbs.twimg.com/profile_images/1380124346543435785/lPjnOIfz_400x400.jpg", width=90, use_container_width=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<label>Date</label>', unsafe_allow_html=True)
        date = st.selectbox("", ["May 20, 2025"], key="date_select", label_visibility="collapsed")
    
    with col2:
        st.markdown('<label>Time</label>', unsafe_allow_html=True)
        time = st.selectbox("", ["AM / PM"], key="time_select", label_visibility="collapsed")
    
    st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Available Events</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="event-card keynote-card">
            <h3>Keynote: <span style="font-weight: normal;">Future of AI</span></h3>
            <p>10:00am - 12:00am</p>
            <p>Seats: 45/602 left</p>
            <div class="view-seats-button">VIEW SEATS</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Keynote", key="keynote_btn"):
            select_event({
                "name": "Keynote (Future of AI)",
                "time": "10:00am - 12:00am"
            })
    
    with col2:
        st.markdown("""
        <div class="event-card workshop-card">
            <h3>Workshop: <span style="font-weight: normal;">Robotics</span></h3>
            <p>2:00pm - 4:00pm</p>
            <p>Seats: 45/602 left</p>
            <div class="view-seats-button">VIEW SEATS</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Workshop", key="workshop_btn"):
            select_event({
                "name": "Workshop (Robotics)",
                "time": "2:00pm - 4:00pm"
            })
    
    col_spacer, col_proceed = st.columns([3, 1])
    
    with col_proceed:
        st.markdown('<div class="proceed-button">', unsafe_allow_html=True)
        proceed_btn = st.button("Proceed →")
        st.markdown('</div>', unsafe_allow_html=True)
        if proceed_btn:
            go_to_seats()
            
    st.markdown('</div>', unsafe_allow_html=True)

# Seats page
elif st.session_state.page == 'seats':
    col1, col2, col3 = st.columns([2,2,1])
    with col2:
        st.image("https://pbs.twimg.com/profile_images/1380124346543435785/lPjnOIfz_400x400.jpg", width=90, use_container_width=False)
    
    col1, col2 = st.columns(2)
    
    # Seating sections display
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="seating-section front-section">
            <h3>Front (UGX 150K)</h3>
            <p>[A1] [A2] ... [F30]</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Front Section", key="front_section"):
            select_seat("A1", "UGX 150,000")
            
        st.markdown("""
        <div class="seating-section balcony-section">
            <h3>Balcony (UGX 35K)</h3>
            <p>[AA1] [AA2] ... [FF24]</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Balcony Section", key="balcony_section"):
            select_seat("AA1", "UGX 35,000")
    
    with col2:
        st.markdown("""
        <div class="seating-section middle-section-blue">
            <h3>Middle (UGX 70K)</h3>
            <p>[G1] [G2] ... [L30]</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Middle Section (70K)", key="middle_section_1"):
            select_seat("G1", "UGX 70,000")
            
        st.markdown("""
        <div class="seating-section middle-section-green">
            <h3>Middle (UGX 350K)</h3>
            <p>[X1] [X2] ... [X16]</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Middle Section (350K)", key="middle_section_2"):
            select_seat("X1", "UGX 350,000")
    
    if st.session_state.selected_seat:
        st.markdown(f"""
        <div class="selection-indicator">
            > Selected: {st.session_state.selected_seat['seat']} - {st.session_state.selected_seat['price']}
        </div>
        """, unsafe_allow_html=True)
    
    col_back, col_spacer, col_confirm = st.columns([1, 2, 1])
    
    with col_back:
        st.markdown('<div class="back-button">', unsafe_allow_html=True)
        back_btn = st.button("Back ←")
        st.markdown('</div>', unsafe_allow_html=True)
        if back_btn:
            go_to_events()
    
    with col_confirm:
        st.markdown('<div class="confirm-button">', unsafe_allow_html=True)
        confirm_btn = st.button("Confirm Reservation 🔖")
        st.markdown('</div>', unsafe_allow_html=True)
        if confirm_btn:
            go_to_confirmation()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Confirmation page
elif st.session_state.page == 'confirmation':
    # Generate ticket data for QR code
    ticket_data = f"Guest: {st.session_state.user_data['name']}\nSession: {st.session_state.selected_event['name']}\nSeat: {st.session_state.selected_seat['seat']}\nPrice: {st.session_state.selected_seat['price']}"
    qr_code = generate_qr_code(ticket_data)
    barcode = generate_barcode()
    
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,2,1])
    with col2:
        st.image("https://pbs.twimg.com/profile_images/1380124346543435785/lPjnOIfz_400x400.jpg", width=90, use_container_width=False)
    
    col1, col2 = st.columns(2)
    
    st.markdown(f"""
    
    <div class="ticket-confirmation">
        <h2 style="text-align: center;">TICKET CONFIRMATION</h2>
        <p><strong>Guest:</strong> {st.session_state.user_data['name']}</p>
        <p><strong>Session:</strong> {st.session_state.selected_event['name']}</p>
        <p><strong>Seat:</strong> {st.session_state.selected_seat['seat']}</p>
        <p><strong>Price:</strong> {st.session_state.selected_seat['price']}</p>
        <div class="qr-code">
            <img src="data:image/png;base64,{qr_code}" style="width: 100px; height: 100px;"/>
        </div>
        <div class="barcode">
            Barcode: {barcode}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_home, col_spacer, col_print = st.columns([1, 2, 1])
    
    with col_home:
        st.markdown('<div class="home-button">', unsafe_allow_html=True)
        home_btn = st.button("Back to Home 🏠")
        st.markdown('</div>', unsafe_allow_html=True)
        if home_btn:
            go_to_login()
    
    with col_print:
        st.markdown('<div class="print-button">', unsafe_allow_html=True)
        print_btn = st.button("Print Ticket 🖨️")
        st.markdown('</div>', unsafe_allow_html=True)
        if print_btn:
            go_to_success()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Success page
elif st.session_state.page == 'success':
    col1, col2, col3 = st.columns([2,2,1])
    with col2:
        st.image("https://pbs.twimg.com/profile_images/1380124346543435785/lPjnOIfz_400x400.jpg", width=90, use_container_width=False)
    
    col1, col2 = st.columns(2)
    
    col_logout, col_spacer, col_home = st.columns([1, 2, 1])
    
    with col_logout:
        st.markdown('<div class="logout-button">', unsafe_allow_html=True)
        logout_btn = st.button("Log Out →")
        st.markdown('</div>', unsafe_allow_html=True)
        if logout_btn:
            st.session_state.user_data = {
                'name': '',
                'email': '',
                'phone': '',
                'affiliation': ''
            }
            st.session_state.selected_event = None
            st.session_state.selected_seat = None
            go_to_login()
    
    with col_home:
        st.markdown('<div class="home-button">', unsafe_allow_html=True)
        home_btn = st.button("Back to Home 🏠", key="home_success")
        st.markdown('</div>', unsafe_allow_html=True)
        if home_btn:
            go_to_login()
    
    st.markdown('</div>', unsafe_allow_html=True)