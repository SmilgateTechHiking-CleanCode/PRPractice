package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.request.WidgetDataRequest;
import com.refactoring.dashboard.api.dto.response.WidgetDataResponse;
import com.refactoring.dashboard.api.utils.enums.WidgetDataType;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class WidgetEventServiceImpl implements WidgetDataService {

    // private final EventClient eventClient;

    @Override
    public WidgetDataResponse getData(WidgetDataRequest request) {
        // result = eventClient.getEventData(request.getWidgetId());
        // 비즈니스 로직
        // WidgetDataResponse 감싸기
        // 반환
        return WidgetDataResponse.builder().data("event").build();
    }

    @Override
    public boolean supports(String type) {
        return WidgetDataType.EVENT.getType().equalsIgnoreCase(type);
    }

    @Override
    public boolean supports(WidgetDataType type) {
        return WidgetDataType.EVENT == type;
    }
}
