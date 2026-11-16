from django import forms


class LyricsGenerationForm(forms.Form):

    LANGUAGE_CHOICES = [
        ('Hindi', 'Hindi'),
        ('Bengali', 'Bengali'),
        ('English', 'English'),
        ('Hinglish', 'Hinglish'),
    ]

    GENRE_CHOICES = [
        ('Romantic', 'Romantic'),
        ('Heartbreak', 'Heartbreak'),
        ('Spiritual', 'Spiritual'),
        ('Devotional', 'Devotional'),
        ('Cinematic', 'Cinematic'),
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Indie', 'Indie'),
    ]

    MOOD_CHOICES = [
        ('Emotional', 'Emotional'),
        ('Nostalgic', 'Nostalgic'),
        ('Peaceful', 'Peaceful'),
        ('Energetic', 'Energetic'),
        ('Heartbreaking', 'Heartbreaking'),
        ('Hopeful', 'Hopeful'),
        ('Devotional', 'Devotional'),
    ]

    VOCAL_CHOICES = [
        ('No preference', 'No preference'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Duet', 'Duet'),
    ]

    DURATION_CHOICES = [
        ('2 minutes', '2 minutes'),
        ('3 minutes', '3 minutes'),
        ('4 minutes', '4 minutes'),
        ('5 minutes', '5 minutes'),
    ]

    STRUCTURE_CHOICES = [
        ('Standard', 'Standard'),
        ('Cinematic', 'Cinematic'),
        ('Short', 'Short / Reel'),
        ('Custom', 'Custom'),
    ]

    song_title = forms.CharField(
        required=False,
        max_length=150
    )

    creative_prompt = forms.CharField(
        required=True,
        min_length=20,
        max_length=3000
    )

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES
    )

    genre = forms.ChoiceField(
        choices=GENRE_CHOICES
    )

    mood = forms.ChoiceField(
        choices=MOOD_CHOICES
    )

    vocal = forms.ChoiceField(
        choices=VOCAL_CHOICES
    )

    duration = forms.ChoiceField(
        choices=DURATION_CHOICES
    )

    structure = forms.ChoiceField(
        choices=STRUCTURE_CHOICES
    )

    instructions = forms.CharField(
        required=False,
        max_length=1500
    )

    def clean_creative_prompt(self):
        prompt = self.cleaned_data['creative_prompt'].strip()

        if not prompt:
            raise forms.ValidationError(
                "Please describe your song idea."
            )

        return prompt

    def clean_song_title(self):
        return self.cleaned_data.get('song_title', '').strip()

    def clean_instructions(self):
        return self.cleaned_data.get('instructions', '').strip()