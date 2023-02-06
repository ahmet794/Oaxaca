import menu_database as db

def run(reset_table=False):
    if reset_table:
        db.create_mains_table()

    #Starters
    db.add_items('TORTILLA CHIPS & SALSAS','Starters', 5.50, 150, True, 'None', 'Served with our homemade roasted salsa and pico de gallo.')
    db.add_items('TORTILLA CHIPS & GUACAMOLE', 'Starters', 6.00, 200, True,'None', 'Our famous guacamole is freshly made every day using fresh ingredients.')
    db.add_items('NACHOS', 'Starters', 7.00, 306, True, 'Cheese, jalepenos', 'Tortilla chips topped with jack cheese, roasted salsa, jalapeño cream cheese, sour cream and our famous guacamole.')
    db.add_items('SOUTHWEST SPRING ROLLS','Starters', 7.00, 239, True, 'Cheese', 'Chipotle Mexican chicken, peppers & jack cheese folded in a flour tortilla, deep fried & served with our famous guacamole.')
    db.add_items('GRILLED CHICKEN WINGS', 'Starters', 7.50, 312, False, 'None', 'Grilled chicken with Lousiana Hot souce.')
    #Mains
    db.add_items('MEXICAN PAELLA', 'Mains', 15.00, 300, False, 'Prawns', 'Slow cooked Mexican rice with tiger prawns, chicken, chorizo, red salsa, peas & sweetcorn. (Hot)')
    db.add_items('SEAFOOD PAELLA', 'Mains', 15.00, 200, False, 'Prawns, Nuts', 'Mexican rice cooked with chorizo, seafood cocktail, black tiger prawns, roasted salsa, peas, sweet corn and fresh coriander. (Hot)')
    db.add_items('MEAT PAELLA', 'Mains', 15.00, 400, False, 'None', 'Slow cooked Mexican rice with chicken, chorizo, red salsa, peas & sweetcorn topped with grilled steak & bacon. (Hot)')
    db.add_items('BEEF CARNITAS ENCHILADA', 'Mains', 14.50, 410, False, 'None', 'olled flour or white corn tortillas (GF) filled with jack cheese, poblano chilli peppers and topped with creamy salsa, jalapeños & cheese. Oven baked and served over a bed of Mexican rice & our famous guacamole.')
    db.add_items('POBLANO CHICKEN', 'Mains', 14.50, 350, False, 'None', 'Grilled chicken breast topped with red salsa, poblano chilli peppers, melted jack cheese, served with seasoned fries.')
    db.add_items('MEX BURGER', 'Mains', 14.50, 600, False, 'Cheese', 'Beef burger folded in a flour tortilla with jack cheese, poblano chilli peppers & Chilli con Carne, served with pico de gallo, sour cream, our famous guacamole & Mexican rice.')
    #Desserts
    db.add_items('ICE CREAM', 'Desserts', 4.00, 145, False, 'Milk', 'Two scoops, choose from vanilla, strawberry, chocolate or toffee.')
    db.add_items('BUNUELOS', 'Desserts', 6.00, 212, False, 'None', 'Fried dough ball dusted with cinnamon sugar served with Dulce de Leche & chocolate fudge sauce.')
    db.add_items('CHOCOLATE BROWNIE', 'Dessert', 6.00, 200, False, 'Milk', 'Warm chocolate fudge brownie served with vanilla ice cream.')
    db.add_items('CHURROS', 'Desserts', 6.50, 256, False, 'Milk', 'Mexican doughnut fried and dusted with cinnamon sugar with a side of Dulce de Leche & vanilla ice cream.')
    db.add_items('BANANA CHIMICHANGA', 'Desserts', 6.50, 200, False, 'Milk', 'A cinnamon flour tortilla filled with banana, deep fried and served with Dulce de Leche & vanilla ice cream.')
    #Soft Drinks, Beers, Ciders
    db.add_items("Coke Zero", "Soft Drinks", 3.30, 0, None, None, None)
    db.add_items("Coca Cola", "Soft Drinks", 3.50, 139, None, None, None)
    db.add_items("Sprite", "Soft Drinks", 3.30, 110, None, None, None)
    db.add_items("Fanta", "Soft Drinks", 3.30, 120, None, None, None)
    db.add_items("Orange Juice", "Soft Drinks", 4.00, 30, None, None, None)
    db.add_items("Budweiser 4.5% ABV", "Beers", 5.50, 186, None, None, None)
    db.add_items("Mahou 5.1% ABV", "Beers", 6.50, 190, None, None, None)
    db.add_items("Corona 4.5% ABV", "Beers", 5.50, 175, None, None, None)
    db.add_items("Stella Cidre", "Ciders", 6.50, 150, None, None, None)
    db.add_items("Stella Cidre Raspberry", "Ciders", 7.00, 190, None, None, None)
