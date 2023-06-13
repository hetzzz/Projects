/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database;
import java.sql.*;
import javax.swing.*;

public class dbclass {
    public static Connection con;
    public static Statement st;
    
    static{
       
    
    try{
    
    con = DriverManager.getConnection("jdbc:mysql://localhost:3306/expmanage","root","1234");
    st = con.createStatement();
    }catch (Exception ex){
        JOptionPane.showMessageDialog(null ,ex);
            }
}
}
