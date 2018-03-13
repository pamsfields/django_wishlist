from django.shortcuts import render
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list(request):

    """If this is a POST request, the user clicked the Add button
    in the form. Check if the new place is valid, if so, save a
    new Place to the database, and redirect to this same page.
    This creates a GET request to this same route.

    If not a POST route, or Place is not valid, display a page with
    a list of places and a form to add a new place.
    """

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save() #create a new Place object from the form
        if form.is_valid(): #Checks for DB constraints violated
            place.save()    #Saves the place to the database
            return redirect('place_list')   #Redirect to a GET request for this same route

    # If not a POST, or the form is not valid, display
    # a page with a list of places and a form to add a new place.
    places = Place.objects.filter(visited=False). order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form': new_place_form})

def places_visted(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visisted = True
        place.save()
    return redirect('place_list')
