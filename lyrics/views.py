from django.shortcuts import render

from .forms import LyricsGenerationForm
# from .services.gemini_service import (
#     generate_song_lyrics,
#     GeminiServiceError
# )
from .services.gemini_service import (
    generate_song_lyrics,
    GeminiServiceError,
    GeminiRateLimitError
)

def dashboard(request):

    context = {
        'total_songs': 0,
        'recent_lyrics': [],
    }

    return render(
        request,
        'lyrics/dashboard.html',
        context
    )


def lyrics_generator(request):

    form = LyricsGenerationForm()
    generated_lyrics = None
    generation_error = None

    if request.method == 'POST':

        form = LyricsGenerationForm(request.POST)

        if form.is_valid():

            try:

                generated_lyrics = generate_song_lyrics(
                form.cleaned_data
                )

            except GeminiRateLimitError as error:

                generation_error = str(error)

            except GeminiServiceError as error:

                generation_error = str(error)

    context = {
        'form': form,
        'generated_lyrics': generated_lyrics,
        'generation_error': generation_error,
    }

    return render(
        request,
        'lyrics/generator.html',
        context
    )