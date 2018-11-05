package backend.backendRealisation.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-05.
 */
public class OrderListDTO {

    private List<OrderDTO> lista_zamowien;

    public List<OrderDTO> getLista_zamowien() {
        return lista_zamowien;
    }

    public void setLista_zamowien(List<OrderDTO> lista_zamowien) {
        this.lista_zamowien = lista_zamowien;
    }
}
