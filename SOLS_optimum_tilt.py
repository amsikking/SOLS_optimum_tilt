import numpy as np

def optimum_tilt(na, n, verbose=True):
    theta_1 = np.arcsin(na/n)
    theta_e = np.arctan(np.sin(theta_1) / (1/(2*np.pi) + np.cos(theta_1)))
    theta_x = theta_1 - theta_e
    theta_t = np.pi/2 - theta_e    
    if verbose:
        print('Optimum tilt (NA=%0.2f, n=%0.2f):'%(na,n))
        print('theta_1=%0.2f'%np.rad2deg(theta_1))
        print('theta_e=%0.2f'%np.rad2deg(theta_e))
        print('theta_x=%0.2f'%np.rad2deg(theta_x))
        print('theta_t=%0.2f'%np.rad2deg(theta_t))
        print('')
    return theta_1, theta_e, theta_x, theta_t

if __name__ == "__main__":
    # Input:
    theta_t_135sil = np.rad2deg(optimum_tilt(1.35, 1.41)[3])
    theta_t_100wat = np.rad2deg(optimum_tilt(1.00, 1.33)[3])

    # Plot:
    na = np.linspace(0.5, 0.96, 1000)
    theta_1, theta_e, theta_x, theta_t = np.rad2deg(
        optimum_tilt(na, 1.00, verbose=False))

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('SOLS optimum tilt')
    ax.set_ylabel('theta_t (deg)')
    ax.set_xlabel('theta_1 (deg)')
    ax.plot(theta_1, theta_t, label='optimum tilt', color='g')
    ax.axvline(x=73.23, label='NA 1.35 sil (%0.2f)'%theta_t_135sil,
               linestyle='--', color='r')
    ax.axvline(x=48.75, label='NA 1.00 wat (%0.2f)'%theta_t_100wat,
               linestyle='-.', color='b')
    ax.axhline(y=55, label='AMS-AGY v2.0 max', linestyle=':', color='k')
    ax.set_ylim(ymin=0)
    plt.legend(loc="lower left")
    fig.savefig('SOLS_optimum_tilt.png', dpi=150)
    plt.show()
