import matplotlib.pyplot as plt


#------------------------------- MAIN CHART CLASS -------------------------------
#---------------------- WILL HOLD ALL FUTURE CHART OBJECTS -------------------------------

class Charts:
    def multiple_plots():
        
        days = list(range(1, 9))
        celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
        celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]

        fig, ax = plt.subplots()

        ax.set(xlabel='Day',
            ylabel='Temperature in Celsius',
            title='Temperature Graph')

        ax.plot(days, celsius_min, label='Min Temperature', color='blue', marker='o')
        ax.plot(days, celsius_max, label='Max Temperature', color='red', marker='o')

        ax.legend()
        return fig