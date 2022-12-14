import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

/*
* STATE MANAGEMENT FOR MESSAGE DATA
*/

interface interceptionDataState{
    data: DataClass;
}
// Generated by https://quicktype.io

export interface DataClass {
    "Http Interceptor":      Interceptor;
    "Websocket Interceptor": Interceptor;
}
export interface Interceptor {
    activated:   boolean;
    intercepted: intercepted[];
    name:        string;
}

export interface intercepted {
    message: string;
    domain:  string;
    reason:  string;
    timestamp: number;
}

const initialState : interceptionDataState = {
    data: {
        "Http Interceptor": {
            activated: true,
            intercepted: [],
            name: "Http Interceptor"
        },
        "Websocket Interceptor": {
            activated: true,
            intercepted: [],
            name: "Websocket Interceptor"
        },
    }
}

export const InterceptionDataSlice = createSlice({
    name: "interceptionData",
    initialState,
    reducers: {
        setInterceptionData: (state, action: PayloadAction<DataClass>) => {
            state.data = action.payload;
            console.log(action.payload);
        }
    }
});

export const { setInterceptionData } = InterceptionDataSlice.actions;

export default InterceptionDataSlice.reducer;


