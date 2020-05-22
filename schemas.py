''' Funções que retornam os schemas de cada tabela '''

def price_quote():
    return {
        "tube_assembly_id":"STRING",
        "supplier":"STRING",
        "quote_date":"DATE",
        "annual_usage":"INTEGER",
        "min_order_quantity":"INTEGER",
        "bracket_pricing":"STRING",
        "quantity":"INTEGER",
        "cost":"FLOAT"
    }

def comp_boss():
    return {
        "component_id":"STRING",
        "component_type_id":"STRING",
        "connection_type_id":"STRING",
        "outside_shape":"STRING",
        "base_type":"STRING",
        "height_over_tube":"STRING",
        "bolt_pattern_long":"STRING",
        "bolt_pattern_wide":"STRING",
        "groove":"STRING",
        "base_diameter":"STRING",
        "shoulder_diameter":"STRING",
        "unique_feature":"STRING",
        "orientation":"STRING",
        "weight":"STRING"
    }

def bill_of_materials():
    return {
        "tube_assembly_id":"STRING",
        "component_id_1":"STRING",
        "quantity_1":"STRING",
        "component_id_2":"STRING",
        "quantity_2":"STRING",
        "component_id_3":"STRING",
        "quantity_3":"STRING",
        "component_id_4":"STRING",
        "quantity_4":"STRING",
        "component_id_5":"STRING",
        "quantity_5":"STRING",
        "component_id_6":"STRING",
        "quantity_6":"STRING",
        "component_id_7":"STRING",
        "quantity_7":"STRING",
        "component_id_8":"STRING",
        "quantity_8":"STRING"
    }