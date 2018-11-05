package backend.backendRealisation.model;

/**
 * Created by Piotr on 2018-11-05.
 */
public class CourseDTO {

    private int id_dania;
    private String nazwa;

    public int getId_dania() {
        return id_dania;
    }

    public void setId_dania(int id_dania) {
        this.id_dania = id_dania;
    }

    public String getNazwa() {
        return nazwa;
    }

    public void setNazwa(String nazwa) {
        this.nazwa = nazwa;
    }
}
