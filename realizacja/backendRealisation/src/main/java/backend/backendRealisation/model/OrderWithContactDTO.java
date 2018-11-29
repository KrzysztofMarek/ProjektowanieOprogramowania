package backend.backendRealisation.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-29.
 */
public class OrderWithContactDTO {

    private int id_zamowienia;
    private List<CourseDTO> lista_dan;
    private String status;
    private ContactDTO kontakt;

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

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public ContactDTO getKontakt() {
        return kontakt;
    }

    public void setKontakt(ContactDTO kontakt) {
        this.kontakt = kontakt;
    }
}
