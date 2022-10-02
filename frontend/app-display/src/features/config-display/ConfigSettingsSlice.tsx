import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { RootState } from "../../app/store";

/*
* STATE MANAGEMENT FOR SETTINGS
*/

interface ConfigSettingsState {
    domains: string[];
    blockedWords: string[];
};

const initialState: ConfigSettingsState = {
    domains: [],
    blockedWords: [],
};

export const configSettingsSlice = createSlice({
    name: "configSettings",
    initialState,
    reducers: {
        setConfigSettings: (state, action: PayloadAction<ConfigSettingsState>) => {
            state = action.payload;
        }
    }
});

export const { setConfigSettings } = configSettingsSlice.actions;

export const selectConfigSettings = (state: RootState) => state.configSettings;
export default configSettingsSlice.reducer;