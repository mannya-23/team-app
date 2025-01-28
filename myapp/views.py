from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import TeamMember
from .serializers import TeamMemberSerializer

# Create your views here.
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

def team_members_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team_members_list.html', {'team_members': team_members})

def add_team_member(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        role = request.POST['role']
        TeamMember.objects.create(
            first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, role=role
        )
        return redirect('team_members_list')
    return render(request, 'add_team_member.html')

def edit_team_member(request, id):
    team_member = get_object_or_404(TeamMember, id=id)
    if request.method == 'POST':
        team_member.first_name = request.POST['first_name']
        team_member.last_name = request.POST['last_name']
        team_member.email = request.POST['email']
        team_member.phone_number = request.POST['phone_number']
        team_member.role = request.POST['role']
        team_member.save()
        return redirect('team_members_list')
    
    return render(request, 'edit_team_member.html', {'team_member': team_member})


def delete_team_member(request, id):
    # Fetch the team member
    team_member = get_object_or_404(TeamMember, id=id)

    # Only allow deletion if the role is 'regular'
    if team_member.role == 'regular':
        team_member.delete()

    # Redirect to the team members list
    return redirect('team_members_list')