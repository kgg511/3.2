Names = 'Gilberto Christiana Amie Vance Denise Rutha Otha Reita Yuriko Jacques Evelina Omar Shizuko Camellia Dede Rozanne Jerlene Loree Shanice Fredric Marietta Tandy Kelli Derek Rochelle Nichelle Nia Nathanael Jeanne Deanne Cherry Carmine Anya Tresa Isa Preston Kimberely Lorrie Elias Caryn Blanche Bunny Darron Laurel Lettie Cori Francesco Shameka Jong Loise Caitlin Thresa Francie Xuan Troy Daron Lavette Astrid Sunshine Pandora Kaye Carlena Prudence Saundra Terence Wilson Renda Mohammad Perry Fumiko Sherika Van Micki Janet Catherin Edgardo Kassie Rebbeca Cherri Pura Madison Jodie Kristie Yael Carlyn Takako Rosina Ashlee Lynetta Thomas Myrtis Kayce Dominick Tenisha Tiffiny Migdalia Sharyl Billy Oma Machelle Kiesha Xochitl Elvie Ardis Whitney Jonie Josiah Valentin Alix Aleshia Maricela Mitchell Rozanne Rosia Sonya Angelita Royce Barbra Jacklyn Evelia Katina Agatha Jaquelyn Cathy Dee Astrid Rikki Scot Sarita Catrice Darrin Brittanie Leena Jerold Kathe Rashida Lyndon Reggie Celestine Jamey Audie Brice Linda Alene Dorian Jenice Muoi Yoshiko Joi Susan'.split()

print('I have a long list of names. Would you like me to print them uppercase or lower case? Type upper or lower to respond')
response = input()
if response.startswith('upper') or response.startswith("Upper"):
   for name in Names:
       print(name.upper())

elif response.startswith('lower') or response.startswith('lower'):
      for name in Names:
          print(name.lower())

else:
    print('please respond with upper/Upper/lower/Lower')
    
