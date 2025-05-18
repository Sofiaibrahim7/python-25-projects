import streamlit as st
import random
import time
from bisect import bisect_left

# --- Searching Methods ---
def naive_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    else:
        return binary_search(lst, target, midpoint + 1, high)

def builtin_bisect_search(lst, target):
    index = bisect_left(lst, target)
    if index != len(lst) and lst[index] == target:
        return index
    return -1

# --- Streamlit App ---
st.set_page_config(page_title="Binary Search Comparison", layout="centered")
st.title("🔍 Binary Search Algorithm Comparison")

st.sidebar.header("Search Settings")

# User input
target = st.sidebar.number_input("Enter a number to search", min_value=-1000, max_value=1000, value=50)
method = st.sidebar.selectbox("Choose search method", ["Naive", "Binary", "Bisect"])

# Generate random list
lst = sorted(random.sample(range(-1000, 1000), 100))

st.write("### 🔢 Sorted List:")
st.code(lst, language="python")

# Perform search
if st.button("🔎 Search Now"):
    if method == "Naive":
        result = naive_search(lst, target)
    elif method == "Binary":
        result = binary_search(lst, target)
    else:
        result = builtin_bisect_search(lst, target)

    if result != -1:
        st.success(f"✅ Target found at index {result}")
    else:
        st.error("❌ Target not found")

# Performance test (optional)
if st.checkbox("📊 Show Performance Test (10000 items)"):
    length = 10000
    big_list = sorted(random.sample(range(-3 * length, 3 * length), length))

    start = time.perf_counter()
    for item in big_list:
        naive_search(big_list, item)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    for item in big_list:
        binary_search(big_list, item)
    binary_time = time.perf_counter() - start

    start = time.perf_counter()
    for item in big_list:
        builtin_bisect_search(big_list, item)
    bisect_time = time.perf_counter() - start

    st.write("### 🕒 Performance (for 10,000 items)")
    st.write(f"🔁 Naive Search Time: `{naive_time:.4f} seconds`")
    st.write(f"📐 Binary Search Time: `{binary_time:.4f} seconds`")
    st.write(f"📦 Bisect Search Time: `{bisect_time:.4f} seconds`")
