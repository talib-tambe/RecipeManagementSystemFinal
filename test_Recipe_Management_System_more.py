import unittest
from Recipe_Management_System import RecipeManager, Recipe



class TestRecipeManager(unittest.TestCase):

    print("Second Test Recipe Management System (Testing Raising Exception Only)")

    def test_add_recipe(self):
        # Let the fields remain empty for testing exception
        print("")
        print("Testing Adding a Recipe")
        print("")
        self.manager = RecipeManager()
        with self.assertRaises(Exception):
            self.manager.add_recipe()

    def test_delete_recipe(self):
        # Trying to delete a non existent recipe
        print("")
        print("Testing Deleting a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)

        with self.assertRaises(Exception):
            self.manager.delete_recipe()  # Enter ID of non existent recipe

    def test_edit_recipe(self):
        # Trying to update a non existent recipe
        print("")
        print("Testing updating a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)

        with self.assertRaises(Exception):
            self.manager.edit_recipe()  # Enter ID of non existent recipe

    def test_import_recipe(self):
        # Import a file with wrong file format i.e, html
        print("")
        print("Testing importing recipe file")
        print("")
        self.manager = RecipeManager()

        with self.assertRaises(Exception):
            # Enter ID of non existent recipe
            self.manager.import_data(file_path='recipes.html')

    def test_export_recipe(self):
        # Export a file with wrong format i.e, CSS
        print("")
        print("Testing exporting recipe file")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        with self.assertRaises(Exception):
            self.manager.export_data(file_format='css')

    def test_view_recipes_filtered_list_only(self):

        print("")
        print("Testing view recipes filtered list only")
        print("")

        fullList = []
        nameList = []
        categoryList = []
        ratingList = []

        self.manager = RecipeManager()

        test_recipe = Recipe(1, "Gajar Ka Halwa", "carrot milk sugar water",
                             "1) mash in blender 2)serve with ice cream", "dessert", "5")
        self.manager.recipes.append(test_recipe)
        fullList.append(test_recipe)
        categoryList.append(test_recipe)
        ratingList.append(test_recipe)

        test_recipe = Recipe(2, "Aloo ka paratha", "potato masala spices",
                             "1) mash in blender 2) Mix with masala and spices", "indian fast food", "4")
        self.manager.recipes.append(test_recipe)
        fullList.append(test_recipe)

        test_recipe = Recipe(3, "arabic mandi", "rice tomato puree",
                             "1) mix tomato with rice 2) steam the rice 3) add whole mutton leg", "arabic food", "5")
        self.manager.recipes.append(test_recipe)
        fullList.append(test_recipe)
        ratingList.append(test_recipe)

        test_recipe = Recipe(4, "burger", "chicken or beef patty lettuce tomato and bun",
                             "1)put all the items over one another 2)apply sauce and mayonise", "fast food", "3")
        self.manager.recipes.append(test_recipe)
        fullList.append(test_recipe)

        test_recipe = Recipe(5, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager.recipes.append(test_recipe)
        nameList.append(test_recipe)
        fullList.append(test_recipe)
        categoryList.append(test_recipe)

        with self.assertRaises(Exception):
            self.assertEqual(self.manager.view_recipe(),
                             nameList)

        with self.assertRaises(Exception):
            self.assertEqual(self.manager.view_recipe(), fullList)

        with self.assertRaises(Exception):
            self.assertEqual(self.manager.view_recipe(), ratingList)

        with self.assertRaises(Exception):
            self.assertEqual(self.manager.view_recipe(), categoryList)
            


if __name__ == '__main__':
    unittest.main()
