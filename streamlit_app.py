import os
from os.path import dirname, abspath

import psycopg2
import streamlit as st

from display_utils import set_background, set_rtl


def validate_non_empty_str(text):
    if text is None or len(text) < 1:
        return False
    return True


def validate_inputs(name, surname, adults_count, children_count, arriving):
    if not validate_non_empty_str(name):
        st.warning('שם חסר')
    if not validate_non_empty_str(surname):
        st.warning('שם משפחה חסר')

    conn = psycopg2.connect(dbname=os.environ['db_name'], user=os.environ['db_user'],
                            password=os.environ['db_pass'], host=os.environ['db_host'],
                            port=os.environ['db_port'])
    cursor = conn.cursor()
    cursor.execute("INSERT INTO guests (name, surname, adults_count, children_count, arriving) "
                   f"VALUES ('{name}', '{surname}', {adults_count}, {children_count}, {arriving})")
    conn.commit()
    cursor.close()
    conn.close()


def create_form():
    name = st.text_input("שם פרטי")
    surname = st.text_input("שם משפחה")
    arriving = st.checkbox("מגיעים?", value=True, key='arriving_toggle')
    if arriving:
        adults_count = st.number_input("כמה מבוגרים תהיו?", key='adults_count', min_value=1, max_value=4, step=1)
        children_count = st.number_input("ילדים?", key='children_count', min_value=0, max_value=4)
    else:
        adults_count = st.number_input("כמה מבוגרים תהיו?", key='adults_count', min_value=0, max_value=0, step=1,
                                       disabled=True)
        children_count = st.number_input("ילדים?", key='children_count', min_value=0, max_value=0,
                                         disabled=True)

    st.button('אישור', on_click=validate_inputs,
              kwargs={'name': name, 'surname': surname, 'adults_count': adults_count,
                      'children_count': children_count, 'arriving': arriving}, disabled=not(name and surname))


if __name__ == '__main__':
    set_rtl(st)
    source_dir = dirname(abspath(__file__))
    set_background(st, os.path.join(source_dir, 'resources', 'background.PNG'))
    create_form()
