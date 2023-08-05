```mermaid
flowchart LR

            style A_group stroke-dasharray: 5 5
            subgraph A
                direction TB 
                A_du["def= <br> use=  "] 
                A_code["potencia(float x, float y) "] 
            end 

            style B_group stroke-dasharray: 5 5
            subgraph B
                direction TB 
                B_du["def= <br> use=  "] 
                B_code["float z; "] 
            end 

            style C_group stroke-dasharray: 5 5
            subgraph C
                direction TB 
                C_du["def= <br> use=  "] 
                C_code["int p; "] 
            end 

            style D_group stroke-dasharray: 5 5
            subgraph D
                direction TB 
                D_du["def= <br> use=  "] 
                D_code["if (y < 0) "] 
            end 

            style E_group stroke-dasharray: 5 5
            subgraph E
                direction TB 
                E_du["def= <br> use=  "] 
                E_code["p = 0 - y; "] 
            end 

            style F_group stroke-dasharray: 5 5
            subgraph F
                direction TB 
                F_du["def= <br> use=  "] 
                F_code["else "] 
            end 

            style G_group stroke-dasharray: 5 5
            subgraph G
                direction TB 
                G_du["def= <br> use=  "] 
                G_code["p = y; "] 
            end 

            style H_group stroke-dasharray: 5 5
            subgraph H
                direction TB 
                H_du["def= <br> use=  "] 
                H_code["z = 1.0; "] 
            end 

            style I_group stroke-dasharray: 5 5
            subgraph I
                direction TB 
                I_du["def= <br> use=  "] 
                I_code["while (p != 0) "] 
            end 

            style J_group stroke-dasharray: 5 5
            subgraph J
                direction TB 
                J_du["def= <br> use=  "] 
                J_code["z = z * x; "] 
            end 

            style K_group stroke-dasharray: 5 5
            subgraph K
                direction TB 
                K_du["def= <br> use=  "] 
                K_code["p = p - 1; "] 
            end 

            style L_group stroke-dasharray: 5 5
            subgraph L
                direction TB 
                L_du["def= <br> use=  "] 
                L_code["if (y < 0) "] 
            end 

            style M_group stroke-dasharray: 5 5
            subgraph M
                direction TB 
                M_du["def= <br> use=  "] 
                M_code["z = 1 / z; "] 
            end 

            style N_group stroke-dasharray: 5 5
            subgraph N
                direction TB 
                N_du["def= <br> use=  "] 
                N_code["print(z); "] 
            end 

            style O_group stroke-dasharray: 5 5
            subgraph O
                direction TB 
                O_du["def= <br> use=  "] 
                O_code["return z; "] 
            end 
```