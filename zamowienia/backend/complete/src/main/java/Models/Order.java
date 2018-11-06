package Models;

import java.sql.Date;
import java.util.ArrayList;

public class Order {

    public Integer id_klienta;
    public Integer id_zamowienia;
    public Integer id_restauracji;
    public ArrayList<OrderItem> lista;
    public double kwota;
    public String status;
    public Date data_dodania;
    public int ocena;

}

