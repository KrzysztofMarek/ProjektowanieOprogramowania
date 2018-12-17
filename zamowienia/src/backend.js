import axios from "axios";

export const oferty = axios.create({ baseURL: "http://localhost:8888/" });
export const zamowienia = axios.create({ baseURL: "http://localhost:8090/" });
export const punkty = axios.create({ baseURL: "http://localhost:8090/" });