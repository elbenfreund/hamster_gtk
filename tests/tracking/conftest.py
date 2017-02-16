# -*- coding: utf-8 -*-

"""Fixtures for unittesting the tracking submodule."""

from __future__ import absolute_import, unicode_literals

import pytest

from hamster_gtk.tracking import screens


@pytest.fixture
def tracking_screen(request, app):
    """Return a plain TrackingScreen instance."""
    return screens.TrackingScreen(app.controller, app.config)


@pytest.fixture
def start_tracking_box(request, app):
    """Provide a plain StartTrackingBox instance."""
    return screens.StartTrackingBox(app.controller, app.config)


@pytest.fixture
def current_fact_box(request, app):
    """Provide a plain CurrentFactBox instance."""
    return screens.CurrentFactBox(app.controller)
