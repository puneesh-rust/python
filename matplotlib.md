# Mathplotlib and Seaborn 

# simple ploting

      cost_car = [list data ]  

      plt.plot(cost_car)

# fixed x nd y axis 

       year = [list od year ]

       plt.plot(cost_car , year)
       plt.xlabel(cost_car)
       plt.ylabel(year)

# important methods 

     1. plt.title gives a title to the chart 
     
     2. plt.legend represent name of graph object 

     3. for gives some mark point use

         plt.plot(cost_car , year   maker =  'o/x')

     4. style and colors 

        color : c
        linestyle : ls (- and -- are used for )
        linewidth : lw
        markerSize : ms 
        markeredgecolor : mec
        markeredgewidth : mew
        markerfacecolor : mfc
        alpha : opacity   

     basic syntax in stying is _
       fmt = [marker] [line] [color] ;

     5. figure size 
          plt.figure(figsize=(2,2))    

     6. plt.plot(year , cost , 'or')     
         it gives dots withpout line:



# SeaBorn 
     styling with seaborn 

         sns.set_style('whitegrid')         

     sns.scatterplot(x=dataset.col , y = dataset.col , hue= dataset.col , s= si
     ze . data= dataset)    
      plt.figure  is same for seaborn for change the figure size 



# histogram 
         plt.hist is used for distribution the column

        for controlling the Size and bins 

        for equal bins 
        import numpy as np
        np.arange(2,5,0.25)

      then plt.hist(new_data.col , bins=np.arange(2,5,0.25));

# bar Chart 

        we can draw bar chart and line both together 

        plt.bar(a,b)      
        plt.plot(c,b , bottom=c)

        # for avg. data we used 

        sns.barplot('day', 'total_bill' , data = file name )

# for 2_d data 

          first data store in varible 
          then called heatmap function 
          sns.heatmap(varible_name)

# Working with image 
     1.from urllib.request import urlretrieve
     2. urlretrieve()        
     3. from PIL import image 
     4. img = Image.open('imageName')
       # it can store in object so we can convert into array 

     5. img_array = np.array(img)   
     # for changing shape 
     6. img_array.shape 

     # for display image 
     7. plt.imshow(img)

     we can control the axis and grid 
     plt.grid(False)
     plt.axis('off')

# plotting multiple charts 
    plt.subplots(2,3 figsize=())     # 2 rows and 3 column 
    plt.tight_layout(pad=2)   # use for giving padding 
    # for accessig 

    axes(0,0) show the first graph.................
    axes(0,1).plot(col1 , col2, 'o--r) second graph
# pairplot 
    A pairplot is a powerful visualization tool in Seaborn that allows you to visualize pairwise relationships between different features in a dataset. It creates a matrix of scatter plots for all pairs of features, along with histograms or KDE plots on the diagonals for each individual feature.

    sns.pairplot(data_set , hue='comparision col)


              