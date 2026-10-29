import streamlit as st


st.set_page_config(
    page_title="Conversor de temperatura",
    page_icon="🌡️",
    layout="centered",
)


def to_celsius(value: float, unit: str) -> float:
    """Convert a temperature to Celsius as an intermediate unit."""
    if unit == "°C":
        return value
    if unit == "°F":
        return (value - 32) * 5 / 9
    return value - 273.15  # K


def from_celsius(value: float, unit: str) -> float:
    """Convert a Celsius temperature to the requested unit."""
    if unit == "°C":
        return value
    if unit == "°F":
        return value * 9 / 5 + 32
    return value + 273.15  # K


st.title("🌡️ Conversor de temperatura")
st.write("Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.")

units = ["°C", "°F", "K"]
col_value, col_from, col_to = st.columns([1.4, 1, 1])

with col_value:
    temperature = st.number_input(
        "Temperatura",
        value=25.0,
        step=1.0,
        format="%.2f",
    )

with col_from:
    source_unit = st.selectbox("Convertir desde", units, index=0)

with col_to:
    target_unit = st.selectbox("Convertir a", units, index=1)

celsius_value = to_celsius(temperature, source_unit)

if celsius_value < -273.15:
    st.error("La temperatura no puede estar por debajo del cero absoluto (−273,15 °C).")
else:
    converted_value = from_celsius(celsius_value, target_unit)
    st.divider()
    st.metric(
        label=f"Resultado en {target_unit}",
        value=f"{converted_value:,.2f} {target_unit}".replace(",", "X").replace(".", ",").replace("X", "."),
    )
    st.caption(
        f"{temperature:g} {source_unit} equivalen a "
        f"{converted_value:.2f} {target_unit}."
    )
