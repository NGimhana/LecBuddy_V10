package LecBuddy_V1;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;


/**
 * Created by Gimhana on 9/27/2017.
 */

public class MainWindow extends JFrame {

    public MainWindow() {
        setSize(500, 400);
        setTitle("Lec Buddy");
        final JPanel main_panel = new JPanel();

        GridLayout grid = new GridLayout(2, 2);
        main_panel.setLayout(grid);

        final JLabel currentImage = new JLabel();
        JLabel convertedImage = new JLabel();

        JButton left_button = new JButton("UPLOAD");

        JButton right_button = new JButton("REFRESH");
        main_panel.add(currentImage);
        main_panel.add(convertedImage);
        main_panel.add(left_button);
        main_panel.add(right_button);

        left_button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                int result = fileChooser.showOpenDialog(main_panel);
                if (result == JFileChooser.APPROVE_OPTION) {
                    String path = fileChooser.getSelectedFile().getAbsolutePath();
                    File file = new File(path);
                    try {
                        BufferedImage image = ImageIO.read(file);
                        Image i = image.getScaledInstance(currentImage.getWidth(), currentImage.getHeight(), Image.SCALE_SMOOTH);
                        ImageIcon icon = new ImageIcon(i);
                        currentImage.setIcon(icon);

                    } catch (IOException e1) {
                        e1.printStackTrace();
                    }
                }

            }
        });

        right_button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                HandWriting.detectText();
            }
        });


        this.add(main_panel);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

}

