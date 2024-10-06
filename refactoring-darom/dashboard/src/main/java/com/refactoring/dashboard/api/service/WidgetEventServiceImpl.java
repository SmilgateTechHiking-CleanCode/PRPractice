package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.response.WidgetEnvetResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class WidgetEventServiceImpl implements WidgetEventService {

    // private final EventClient eventClient;

    @Override
    public WidgetEnvetResponse getEventData(String widgetId) {
        // return eventClient.getEventData(widgetId);
        return null;
    }
}
