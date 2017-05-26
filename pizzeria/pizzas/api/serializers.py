from rest_framework import serializers
from pizzas.models import Ingredient, Pizza, Comment

import json

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Pizza
        fields = "__all__"
    def create(self, validated_data):
        ingredient_data = self.initial_data.pop['ingredients']
        ingredient_data = json.loads(ingredient_data)
        ingredient_parsed = list(map(lambda c: json.loads(c), ingredient_data))
        validated_data.pop('ingredients')
        validated_data.pop('comments')
        pizza = Pizza.objects.create(**validated_data)
        for ingred in ingredient_parsed:
            exist = Ingredient.objects.get(name=ingred["name"])
            pizza.ingredients.add(exist)
        return pizza