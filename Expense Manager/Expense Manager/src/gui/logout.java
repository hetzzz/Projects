/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gui;
import javax.swing.JFrame;
/**
 *
 * @author Het
 */
public class logout {
    public static void logout(JFrame context,login loginscreen ){
     loginsession.isLoggedIn = false;
     context.setVisible(false);
     loginscreen.setVisible(true);
     
     
    }
}
