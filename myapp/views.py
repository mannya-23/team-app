from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import TeamMember
from .serializers import TeamMemberSerializer

# Create your views here.

# View for API operations on team members
class TeamMemberViewSet(viewsets.ModelViewSet):
    # Get all team members
    queryset = TeamMember.objects.all()
    # Format data to JSON
    serializer_class = TeamMemberSerializer

# View to display all team members
def team_members_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team_members_list.html', {'team_members': team_members})

# View to add a new team member
def add_team_member(request):
    # Get the form data if form is submitted
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        role = request.POST['role']

        # Create a new team member and save it to the database
        TeamMember.objects.create(
            first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, role=role
        )

        # Go back to team member list page
        return redirect('team_members_list')
    return render(request, 'add_team_member.html')

# View to edit an existing team member
def edit_team_member(request, id):
    # Gets the team member
    team_member = get_object_or_404(TeamMember, id=id)

    # If form is submitted, update team member info with the new data
    if request.method == 'POST':
        team_member.first_name = request.POST['first_name']
        team_member.last_name = request.POST['last_name']
        team_member.email = request.POST['email']
        team_member.phone_number = request.POST['phone_number']
        team_member.role = request.POST['role']
        
        # Save new data to database
        team_member.save()

        # Go back to team member list page
        return redirect('team_members_list')
    
    return render(request, 'edit_team_member.html', {'team_member': team_member})

# View to delete team member
def delete_team_member(request, id):
    # Get the team member
    team_member = get_object_or_404(TeamMember, id=id)

    # Only allow deletion if the role is 'regular'
    if team_member.role == 'regular':
        team_member.delete()

    # Redirect to the team members list
    return redirect('team_members_list')