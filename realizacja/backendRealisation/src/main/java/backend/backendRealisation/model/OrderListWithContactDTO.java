package backend.backendRealisation.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-29.
 */
public class OrderListWithContactDTO {

    private List<OrderWithContactDTO> lista_zamowien;


    public List<OrderWithContactDTO> getLista_zamowien() {
        return lista_zamowien;
    }

    public void setLista_zamowien(List<OrderWithContactDTO> lista_zamowien) {
        this.lista_zamowien = lista_zamowien;
    }
}
