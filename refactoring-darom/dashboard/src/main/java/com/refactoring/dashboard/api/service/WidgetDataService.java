package com.refactoring.dashboard.api.service;

import com.refactoring.dashboard.api.dto.request.WidgetDataRequest;
import com.refactoring.dashboard.api.dto.response.WidgetDataResponse;
import com.refactoring.dashboard.api.utils.enums.WidgetDataType;

public interface WidgetDataService {

    WidgetDataResponse getData(WidgetDataRequest reuqest);

    boolean supports(String type);

    boolean supports(WidgetDataType type);
}
