package backend.backendReport.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-05.
 */
public class OrderDTO {

    private int id_zamowienia;
    private List<CourseDTO> lista_dan;
    private String status;
    private String miasto;
    private Long czas_realizacji;
    private Long czas_dostawy;


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


    public int getId_zamowienia() {
        return id_zamowienia;
    }

    public void setId_zamowienia(int id_zamowienia) {
        this.id_zamowienia = id_zamowienia;
    }

    public List<CourseDTO> getLista_dan() {
        return lista_dan;
    }

    public void setLista_dan(List<CourseDTO> lista_dan) {
        this.lista_dan = lista_dan;
    }


    public String getMiasto() {
        return miasto;
    }

    public void setMiasto(String miasto) {
        this.miasto = miasto;
    }

    public Long getCzas_realizacji() {
        return czas_realizacji;
    }

    public void setCzas_realizacji(Long czas_realizacji) {
        this.czas_realizacji = czas_realizacji;
    }

    public Long getCzas_dostawy() {
        return czas_dostawy;
    }

    public void setCzas_dostawy(Long czas_dostawy) {
        this.czas_dostawy = czas_dostawy;
    }
}
