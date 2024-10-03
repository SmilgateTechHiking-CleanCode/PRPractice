protected boolean HashMap addMeals(HashMap orderMap) throws Exception{

    //...
    
    //shipping_dt 기준으로 due_date를 구분하는데 due_date와 TIMES_WEEK(1 : 주 2회 2: 주 3회)를 계싼해서 해당 일자의 주문을 생성한다.    
    CommandMap mealMap = new CommandMap();
    mealMap.putAll(orderMap);
    
    List<HashMap> mealList = (List<HashMap>) dao.selectList("subscribeOrderCreate.getSbSubscribeItems", mealMap);
    
    int personVol = StringUtil.nvlInt(orderMap.get("PERSON_VOL"));
    int shippingCnt = 2;
    if("2".equals(StringUtil.nvl(orderMap.get("TIMES_WEEK")))){ // 2: 주 3회
        shippingCnt = 3;
    }
    if("0".equals(StringUtil.nvl(orderMap.get("MEAL_TYPE")))) {
        shippingCnt = 1;
    }
    
    //...
    
    
    
    
    
    //배송 인분수
    for(int p=0; p<personVol; p++){
        for(int i=0; i<shippingCnt; i++){
            //식단 배송일자
            mealMap.put("MENU_DATE", StringUtil.nvl(orderMap.get("DUE_DATE"+i)));   // 1. 해당 부분의 앞 쿼리에서 due_date로 배송 날짜 받은걸 menu_date로 넣는다
            //식단 상세 등록
            for(int j=0; j<mealList.size(); j++){
                HashMap mealData = mealList.get(j);
                mealMap.put("MEAL_TYPE", StringUtil.nvl(mealData.get("MEAL_TYPE")));
                int qty = StringUtil.nvlInt(mealData.get("QTY"));
                List<HashMap> mealItemList = null;
                if("0".equals(StringUtil.nvl(mealData.get("MEAL_TYPE")))){  //MEAL_TYPE 0:마켓구독, 1:저당, 2:라이트 ... 오라클 테이블에 description에 명시돼있음
                    mealItemList = (List<HashMap>)dao.selectList("subscribeOrderCreate.getMarketList", mealMap);
                }
                else{
                    //2.menu_date를 가지고 해당 날짜의 식단 구성을 가져온다.
                    //롯데택배, 새벽배송 휴무일을 체크해서 정상인 날짜에만 생성하는 구문이 subscribeOrderCraete.getMealList where절에 있ㅇ므
                    mealItemList = (List<HashMap>)dao.selectList("subscribeOrderCreate.getMealList", mealMap);
                }
                //3. 이후 가져온 정보를 바탕으로 od_order_detl 데이터를 생성한다.
    
                /**
                 * 
                 * 문제가 생긴 부분
                 * qty가 4인 경우가 생겼을때 itemCnt ArrayIndexOutOfBoundsException 발생
                 */
                if(mealItemList.size() > 0){
                    int itemCnt[] = {0,1,2};
                    String odOrderDetlGrpId ="";
                    if(mealItemList.size() == 1){
                        itemCnt[1] = 0;
                        itemCnt[2] = 0;
                    } else if(mealItemList.size() == 2){
                        itemCnt[2] = 1;
                    }
                    for(int k=0; k<qty; k++){
                        //OD_ORDER_DETL GRP_ID 생성
                        if(k ==0){
                            odOrderDetlGrpId = (String)dao.selectOne("subscribeOrderCreate.getOdOrderDetlGrpId");
                        }
                        else if(itemCnt[k-1] != itemCnt[k]){
                            odOrderDetlGrpId = (String)dao.selectOne("subscribeOrderCreate.getOdOrderDetlGrpId");
                        }
                        HashMap mealItem = new HashMap();
                        mealItem.putAll(mealItemList.get(itemCnt[k]));
                       //... 
                    }
                }
            }
            
    
        }
    }
    
    
    
    }