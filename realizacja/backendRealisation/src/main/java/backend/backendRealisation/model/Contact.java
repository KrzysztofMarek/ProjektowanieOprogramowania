package backend.backendRealisation.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class Contact {

    private String name;
    private String surname;
    private String phoneNumber;
    private String adress;

    public Contact(String name, String surname, String phoneNumber, String adres) {
        this.adress = adres;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.surname = surname;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getAdres() {
        return adress;
    }

    public void setAdres(String adres) {
        this.adress = adres;
    }
}
