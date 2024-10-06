package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetGridResponse;
import org.springframework.stereotype.Service;

@Service
public class WidgetGridServiceImpl implements WidgetGridService {

    // private final GridClient gridClient;

    @Override
    public WidgetGridResponse getGridData(String widgetId) {
        // return gridClient.getGridData(widgetId);
        return null;
    }
}
