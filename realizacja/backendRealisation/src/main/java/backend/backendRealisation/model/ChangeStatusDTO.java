package backend.backendRealisation.model;

/**
 * Created by Piotr on 2018-11-05.
 */
public class ChangeStatusDTO {

    private int id_zamowienia;
    private String status;

    public ChangeStatusDTO(int id_zamowienia, String status) {
        this.id_zamowienia = id_zamowienia;
        this.status = status;
    }

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
}
