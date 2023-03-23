import unittest
from Recipe_Management_system import RecipeManager, Recipe
from unittest.mock import patch


class TestRecipeManager(unittest.TestCase):

    print("First Test Recipe Management System")

    def test_import_recipe(self):
        print("")
        print("Testing importing recipe file")
        print("")
        self.manager = RecipeManager()
        self.manager.import_data(file_path='recipes.csv')
        self.assertEqual(len(self.manager.recipes), 5)

    def test_export_recipe(self):
        print("")
        print("Testing exporting recipe file")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.manager.export_data(file_format='csv')
    
    @patch('builtins.input', side_effect=["kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3"])
    def test_add_recipe(self,mock_input):
        print("")
        print("Testing Adding a Recipe")
        print("")
        self.manager = RecipeManager()
        self.manager.add_recipe()
        self.assertEqual(len(self.manager.recipes), 1)

    @patch('builtins.input', side_effect=["500"])
    def test_delete_recipe(self,mock_input):
        print("")
        print("Testing Deleting a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.manager.delete_recipe()
        self.assertEqual(len(self.manager.recipes), 0)

    @patch('builtins.input', side_effect=["500","sherbet", "milk rose syrup tadpoles",
                             "1) mix evrything and boom", "refereshener", "4"])
    def test_edit_recipe(self,mock_input):
        print("")
        print("Testing editing a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.assertTrue(self.manager.edit_recipe())

    @patch('builtins.input', side_effect=["1","4","kunafa","3","dessert","2","5"])
    def test_view_recipes_filtered_list_only(self,mock_input):

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

        self.assertEqual(self.manager.view_recipe(),
                         fullList)  # Display full list
        # Display by name  Kunafa only
        self.assertEqual(self.manager.view_recipe(), nameList)
        # Display by category dessert only
        self.assertEqual(self.manager.view_recipe(), categoryList)
        # Display by rating 5 only
        self.assertEqual(self.manager.view_recipe(), ratingList)


if __name__ == '__main__':
    unittest.main()
