from rest_framework import serializers

from apiBackend.models import Exercise, List_exercises_category, List_options_exercise

class ExerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id_exercise': instance.id,
            'exercise': instance.exercise,
            'instruction': instance.instruction,
            'phrase_translate':instance.phrase_translate,
            'score': instance.score,
            'message_motivation': instance.message_motivation.message,
        }


class ExerciseByCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = List_exercises_category
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id_detail': instance.id,
            'id_exercise': instance.exercise.id,
            'type_exercise': instance.exercise.type_exercise.id,
            'exercise': instance.exercise.exercise,
            'icon_name': instance.exercise.icon_name,
            'is_solved':instance.is_solved,
        }


class OptionsByExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = List_options_exercise
        exclude = ('state',)
    
    def to_representation(self, instance):
        return {
            'option': instance.option.option,
            'is_correct': instance.option.is_correct,
        }