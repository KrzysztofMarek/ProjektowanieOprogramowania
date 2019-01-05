package Models;

import java.sql.Date;
import java.util.ArrayList;

public class NewOrder {

    public String id_klienta;
    public Integer id_restauracji;
    public ArrayList<OrderItem> lista_dan;
    public Double kwota;
    public String adres;
    public Integer punkty;
}