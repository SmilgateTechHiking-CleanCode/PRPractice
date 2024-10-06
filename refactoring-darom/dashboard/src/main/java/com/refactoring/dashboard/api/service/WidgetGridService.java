package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetGridResponse;

public interface WidgetGridService {
    WidgetGridResponse getGridData(String widgetId);
}
