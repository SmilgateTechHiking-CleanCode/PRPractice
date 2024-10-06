package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.request.WidgetDataRequest;
import com.refactoring.dashboard.api.dto.response.WidgetDataResponse;
import com.refactoring.dashboard.api.utils.enums.WidgetDataType;
import org.springframework.stereotype.Service;

@Service
public class WidgetGridServiceImpl implements WidgetDataService {

    // private final GridClient gridClient;

    @Override
    public WidgetDataResponse getData(WidgetDataRequest request) {
        // result = eventClient.getEventData(request.getWidgetId());
        // 비즈니스 로직
        // WidgetDataResponse 감싸기
        // 반환
        return WidgetDataResponse.builder().data("grid").build();
    }

    @Override
    public boolean supports(String type) {
        return WidgetDataType.GRID.getType().equalsIgnoreCase(type);
    }

    @Override
    public boolean supports(WidgetDataType type) {
        return WidgetDataType.GRID == type;
    }
}
