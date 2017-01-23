from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(
        request,
        'music/detail.html',
        {'album': album}
    )

def favourite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(
            request,
            'music/detail.html',
            {
                'album': album,
                'error_message' : "You did not selected a valid song.",
            }
        )
    else:
        # updating fav song
        selected_song.is_favourite = True
        selected_song.save()

        return render(
            request,
            'music/detail.html',
            {'album': album}
        )
