package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetEnvetResponse;

public interface WidgetEventService {

    WidgetEnvetResponse getEventData(String widgetId);
}
