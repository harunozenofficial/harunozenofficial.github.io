from django.urls import path

from . import views

# from .feeds import LatestMatchesFeed, LatestVideosFeed

urlpatterns = [
    # # PAGES
    # path("", views.MatchesListView.as_view(), name="index"),
    # path("history", views.MatchesHistoryListView.as_view(), name="history"),
    # path("teams", views.TeamsListView.as_view(), name="teams-list"),
    # path("<slug:slug>", views.MatchDetailView.as_view(), name="match-detail"),
    # path("teams/<slug:slug>", views.TeamsDetailView.as_view(), name="teams-detail"),
    # # API
    # path("api/matches/", views.MatchesApiListView.as_view(), name="api-matches-list"),
    # path("api/matches/<slug:slug>", views.MatchesApiDetailView.as_view(), name="api-match-detail"),
    # path(
    #     "api/matches-search-week/",
    #     views.MatchWeekSearchView.as_view(),
    #     name="api-matches-search-week",
    # ),
    # path("api/teams/", views.TeamSearchView.as_view(), name="api-teams-list"),
    # path("api/teams/<slug:slug>", views.TeamApiDetailView.as_view(), name="api-teams-detail"),
    # # RSS
    # path("rss/matches", LatestMatchesFeed()),
    # path("rss/videos", LatestVideosFeed()),
    path("api/videogoals-per-day/", views.videogoals_per_day, name="videogoals_per_day"),
]
