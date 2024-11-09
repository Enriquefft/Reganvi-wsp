"""Materials Valorization data."""

from typing import TypedDict


class MaterialData(TypedDict):
    """Material data structure."""

    item_id: int
    material: str
    price_kg: float
    price_ton: float


def transform_material_data(material_data: list[MaterialData]) -> str:
    """Transform the material data into a format understandable by GPT-4o."""
    transformed_data = "Materials data:\n"
    for material in material_data:
        transformed_data += (
            f"Item ID: {material['item_id']}, "
            f"Material name: {material['material']}, "
            f"Price per kg: {material['price_kg']} PEN, "
            f"Price per ton: {material['price_ton']} PEN.\n"
        )
    return transformed_data


material_data: list[MaterialData] = [
    {"item_id": 1, "material": "PAPEL BLANCO", "price_kg": 0.71, "price_ton": 710.00},
    {
        "item_id": 2,
        "material": "PERIODICO DE PRIMERA",
        "price_kg": 0.85,
        "price_ton": 850.00,
    },
    {
        "item_id": 3,
        "material": "COBRE BRILLANTE",
        "price_kg": 28.00,
        "price_ton": 28000.00,
    },
    {"item_id": 4, "material": "BRONCE", "price_kg": 14.00, "price_ton": 14000.00},
    {
        "item_id": 5,
        "material": "BATERIA CHICA",
        "price_kg": 15.00,
        "price_ton": 15000.00,
    },
    {
        "item_id": 6,
        "material": "BATERIA NORMAL",
        "price_kg": 19.00,
        "price_ton": 19000.00,
    },
    {
        "item_id": 7,
        "material": "BATERIA TORTUGA",
        "price_kg": 25.00,
        "price_ton": 25000.00,
    },
    {
        "item_id": 8,
        "material": "CHATARRA LIVIANA",
        "price_kg": 0.81,
        "price_ton": 810.00,
    },
    {
        "item_id": 9,
        "material": "CHATARRA PESADA",
        "price_kg": 0.72,
        "price_ton": 720.00,
    },
    {"item_id": 10, "material": "BOTELLAS PET", "price_kg": 2.10, "price_ton": 2100.00},
    {
        "item_id": 11,
        "material": "PLASTICO DURO",
        "price_kg": 1.56,
        "price_ton": 1560.00,
    },
    {
        "item_id": 12,
        "material": "PLASTICO FILL LIMPIO",
        "price_kg": 2.00,
        "price_ton": 2000.00,
    },
    {
        "item_id": 13,
        "material": "PLASTICO FILL SUCIO",
        "price_kg": 1.00,
        "price_ton": 1000.00,
    },
    {
        "item_id": 14,
        "material": "ALUMINIO LIVIANO",
        "price_kg": 5.00,
        "price_ton": 5000.00,
    },
    {
        "item_id": 15,
        "material": "ALUMINIO PESADO",
        "price_kg": 5.50,
        "price_ton": 5500.00,
    },
    {"item_id": 16, "material": "PVC", "price_kg": 1.25, "price_ton": 1250.00},
    {"item_id": 17, "material": "CARTON", "price_kg": 0.52, "price_ton": 520.00},
    {
        "item_id": 18,
        "material": "PAPEL MIXTO COLOR",
        "price_kg": 0.65,
        "price_ton": 650.00,
    },
    {"item_id": 19, "material": "VIDRIO", "price_kg": 0.31, "price_ton": 310.00},
    {"item_id": 20, "material": "TETRAPACK", "price_kg": 0.85, "price_ton": 850.00},
    {"item_id": 21, "material": "CARTOPLAS", "price_kg": 1.00, "price_ton": 1000.00},
    {"item_id": 22, "material": "MADERA LEÑA", "price_kg": 1.00, "price_ton": 1000.00},
    {
        "item_id": 23,
        "material": "LONA (ZAPATILLA)",
        "price_kg": 1.51,
        "price_ton": 1510.00,
    },
    {"item_id": 24, "material": "COCALATA", "price_kg": 5.51, "price_ton": 5510.00},
    {
        "item_id": 25,
        "material": "CAUCHOS (LLANTAS)",
        "price_kg": 0.10,
        "price_ton": 100.00,
    },
    {
        "item_id": 26,
        "material": "PAPEL DE REVISTA",
        "price_kg": 0.40,
        "price_ton": 400.00,
    },
    {"item_id": 27, "material": "ALTO IMPACTO", "price_kg": 0.50, "price_ton": 500.00},
    {"item_id": 28, "material": "ACERO", "price_kg": 3.51, "price_ton": 3510.00},
    {
        "item_id": 29,
        "material": "PET PRESADO COLORES",
        "price_kg": 0.70,
        "price_ton": 700.00,
    },
    {
        "item_id": 30,
        "material": "PET PRESADO YOGURT",
        "price_kg": 0.61,
        "price_ton": 610.00,
    },
    {
        "item_id": 31,
        "material": "PET PRESADO ACEITE",
        "price_kg": 0.60,
        "price_ton": 600.00,
    },
    {
        "item_id": 32,
        "material": "TAPITAS DE BOTELLA",
        "price_kg": 1.00,
        "price_ton": 1000.00,
    },
    {
        "item_id": 33,
        "material": "TAPITAS MOLIDA LIMPIA",
        "price_kg": 1.45,
        "price_ton": 1450.00,
    },
]

formatted_material_data = transform_material_data(material_data)
