import numpy as np

NYU_13_CLASSES = ['Unknown', 'Bed', 'Books', 'Ceiling', 'Chair',
                  'Floor', 'Furniture', 'Objects', 'Picture',
                  'Sofa', 'Table', 'TV', 'Wall', 'Window'
                 ]

#NYU_13_CLASSES = [(0,'Unknown'),
#                  (1,'Bed'),
#                  (2,'Books'),
#                  (3,'Ceiling'),
#                  (4,'Chair'),
#                  (5,'Floor'),
#                  (6,'Furniture'),
#                  (7,'Objects'),
#                  (8,'Picture'),
#                  (9,'Sofa'),
#                  (10,'Table'),
#                  (11,'TV'),
#                  (12,'Wall'),
#                  (13,'Window')
#]

colour_code = np.array([[0, 0, 0],
                       [0, 0, 1],
                       [0.9137,0.3490,0.1882], #BOOKS
                       [0, 0.8549, 0], #CEILING
                       [0.5843,0,0.9412], #CHAIR
                       [0.8706,0.9451,0.0941], #FLOOR
                       [1.0000,0.8078,0.8078], #FURNITURE
                       [0,0.8784,0.8980], #OBJECTS
                       [0.4157,0.5333,0.8000], #PAINTING
                       [0.4588,0.1137,0.1608], #SOFA
                       [0.9412,0.1373,0.9216], #TABLE
                       [0,0.6549,0.6118], #TV
                       [0.9765,0.5451,0], #WALL
                       [0.8824,0.8980,0.7608]])

def output(filename, dic):
    with open(filename, "w+") as f:
        f.write("#pragma once\n")
        f.write("#include <map>\n")
        f.write('#include <ORUtils/Vector.h>\n')
        f.write("#include <string>\n\n")        
                
        f.write("\n\n")        
        f.write("static std::map<std::string, unsigned short> wnid_to_NYU13classid {\n")
        f.write("\t{\"\", 0}, \n")
        for a,b in sorted(dic.items()):    
            f.write("\t{\"%s\", %i}, \n" % (a, b))
        f.write("};\n")
            
        f.write("\n\n")
        f.write("static std::map<unsigned short, std::string> NYU13{\n")
        for i in range(len(NYU_13_CLASSES)): 
            f.write("\t{%i, \"%s\"}, \n" % (i, NYU_13_CLASSES[i]))
        f.write("};\n")
            
        f.write("\n\n")
        f.write('static std::map<unsigned short, ORUtils::Vector4<float>> NYU13ColorLabel {\n')
        for x in range(0, colour_code.shape[0]):
            f.write('{' + str(x) + ', ' + 'ORUtils::Vector4<float>(' + str(colour_code[x][0]) + ', ' + str(colour_code[x][1]) + ', ' + str(colour_code[x][2]) + ', 255)},\n')
        f.write("};\n")
            
def output_name2wnid(filename,dic):
    with open(filename, "a+") as f:
        f.write("\n\n")        
        f.write("static std::map<std::string, unsigned short> name_to_wnid {\n")
        for a,b in sorted(dic.items()):    
            f.write("\t{\"%s\", \"%s\"}, \n" % (a, b))
        f.write("};\n")

if __name__ == '__main__':
    # Change these two variables if new columns are added to the wnid_to_class.txt file
    # This is the name of the column in the textfile
    column_name = '13_classes'
    name_name = 'name'
    # This is the list of classes, with the index in the list denoting the # class_id
    class_list = NYU_13_CLASSES

    wnid_to_classid = {}
    name_to_wnid = {}
    with open('wnid_to_class.txt','r') as f:
        class_lines = f.readlines()
        column_headings = class_lines[0].split()
        for class_line in class_lines[1:]:
            wnid = class_line.split()[0].zfill(8)
            classid = class_list.index(class_line.split()[column_headings.index(column_name)])
            wnid_to_classid[wnid] = classid
            name = class_line.split()[1]
            name = name[:name.find('.')]
            name_to_wnid[name] = wnid

    print(wnid_to_classid)
    output("./SceneNet_wnid_to_13labels.h", wnid_to_classid)
    output_name2wnid("./SceneNet_wnid_to_13labels.h", name_to_wnid)


