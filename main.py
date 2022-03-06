import tkinter as tk
import Groups
length = 91





    

def form(Number,abrev,mass,group,melt,boil,dence,color,radius,isotopes,discovered,uses,halflife='Stable'):
        Atomicnumber = float(Number)
        Elementsinsamefamily = Groups.groups[group]

        if Atomicnumber < 118:
            period = '7'
            if Atomicnumber < 87:
                period = '6'
                if Atomicnumber < 55:
                    period = '5'
                    if Atomicnumber < 37:
                        period = '4'
                        if Atomicnumber < 19:
                            period = '3'
                            if Atomicnumber < 11:
                                period = '2'
                                if Atomicnumber < 3:
                                    period = '1'

        if Atomicnumber == 43 or Atomicnumber == 61 or Atomicnumber > 82:
            Radioactive = 'Yes'
        else:
            Radioactive = 'No'
        
        if Atomicnumber > 92:
            Manmade = 'Yes'
        else:
            Manmade = 'No'
        if  Atomicnumber >96:
            State = 'Solid'
            if Atomicnumber > 103:
                State = 'Unknown'

        else:    

            Meltcalc = float(melt)
            Boilcalc = float(boil)
            if Meltcalc > 22.22:
                State = 'Solid'
            if Meltcalc < 22.22 and Boilcalc > 22.22:
                State = 'Liquid'
            if Boilcalc < 22.22:
                State = 'Gas'
        if group == 'Noble Gases':
            Inert = 'Yes'
        else:
            Inert = 'No'
        New_Number = int(Number)
        New_mass = float(mass)
        NeutronsCalc = New_mass - New_Number
        Neutrons = int(round(NeutronsCalc,0))

        result = "Atomic Number:{} \nAbbreviation:{} \nAtomic Mass:{} u \nGroup:{} \nElements in same Group:{}\nPeriod:{}  \nProtons:{} \nNeutrons:{} \nElectrons: {} \nMelting Point: {} °C \nBoiling Point:{} °C \nInert:{} \nState of matter at room temperature:{} \nDensity:{}kg/Meters Cubed \nColor:{} \nAtomic Radius:{} Pm \nRadioactive: {} \nMan Made:{} \nNumber of Known Isotopes:{} \nHalf Life:{}\nDiscovered:{} \nUses:{}".format(Number,abrev,mass,group,Elementsinsamefamily,period,Number,Neutrons,Number,melt,boil,Inert,State,dence,color,radius,Radioactive,Manmade,isotopes,halflife,discovered,uses)
        return result

Elements = {"Hydrogen": form('1', 'H', '1.008', 'Reactive Nonmetals', '-259.1', '-252.9', '0.0899', 'None', '53','7','1766','Hydrogen is used in Tritium Watches and Sun Fusion'),
            "Helium": form('2', 'HE', '4.0026', 'Noble Gases', '-272.2', '-269', '0.1785', 'None', '31','7','1895','Helium is used in Balloons,Blimps,and Helium-ion and Helium Neon lasers'),
            "Lithium": form('3', 'LI', '6.94', 'Alkali Metals', '180.54', '1342', '535', 'Silver', '167','9','1817','Lithium is used in Lithium Batteries and Lithium Carbonate Pills'),
            'Beryllium': form('4', 'BE', '9.0122', 'Alkaline Earth Metals', '1287', '2470', '1848', 'SlateGray', '112','11','1797','Berylium is used in Beryllium Copper golf clubs and Berylium oxide high voltage insulators'),
            "Boron": form('5', 'B', '10.81', 'Metalloids', '2075', '4000', '2460', 'Black', '87','13','1808','Boron is used in Silly putty and Boric acid'),
            "Carbon": form('6', 'C', '12.011', 'Reactive Nonmetals', '3642', '3642', '2260', 'Black', '67','14','3750 bce','Carbon is used for Metal Smelting,and is in the Coal fossil fuels we use'),
            "Nitrogen": form('7', 'N', '14.007', 'Reactive Nonmetals', '-210.1', '-195.8', '1.251', 'None', '56','15','1772','Nitrogen is used in Nitrogen pills for angina and Nitrogen gas canisters'),
            "Oxygen": form('8', "O", '15.999', 'Reactive Nonmetals', '-218', '-183', '1.429', 'None', '48','16','1774','Oxygen is used in Oxygen tanks,andHigh pressure Portable oxygen tanks'),
            "Fluorine": form('9', "F", '18.998', 'Reactive Nonmetals', '-220', '-188.1', '1', 'None', '42','17','1886','Fluorine is used in Toothpaste and Fluroine Salts'),
            "Neon": form('10', 'Ne', '20.180', 'Noble Gases', '-248.6', '-246.1', '0.9', 'None', '38','18','1898','Neon is used in Neon lights and Helium Neon lasers'),
            "Sodium": form('11', "NA", '22.990', 'Alkali Metals', '97.72', '882.9', '968', 'Silver', '190','19','1807','Sodium is used in the creation of Table salt,while Sodium Carbonate is used in water softners'),
            'Magnesium': form('12', "MG", '24.305', 'Alkaline Earth Metals', '650', '1090', '1738', 'Silver', '145','21','1755','Magnesium is used in Laptops andcameras'),
            "Aluminum": form('13', 'AL', '26.982', 'Post Transition Metals', '660.32', '2519', '2700', 'Silver', '118','21','1825','aluminum is used in a few products,Aluminum Sheets and Cans are the most famous'),
            "Silicon": form('14', "Si", '28.085', 'Metalloids', '1414', '2900', '2330', 'Gray', '111','22','1824','silicon is used in Computer chips and alloys for aluminum-silicon and ferro-silicon'),
            "Phosphorus": form('15', 'P', '30.974', 'Reactive Nonmetals', '44.15', '280.5', '1823', 'None', '98','22','1669','phosphorus is used in certain incendiary devices and fertilizers'),
            "Sulfer": form('16', 'S', '32.06', 'Reactive Nonmetals', '115.21', '444.72', '1960', 'Yellow', '88','23','500 bce','sulfur is used in the proccess of vulcanisation of black rubber,production of sulfuric acid.'),
            "Chlorine": form('17', "CL", '35.45', 'Reactive Nonmetals', '-101.5', '-34.040', '3.214', 'Yellow', '79','23','1774','Disenfecting surfaces and Organic Chemistry '),
            "Argon": form('18', "AR", '39.948', 'Noble Gases', '-189', '-186', '1.784', 'None', '71','23','1894','production of reactive elements,fluorescent light bulbs'),
            "Potassium": form('19', "K", '39.098', 'Alkali Metals', '63.38', '758.9', '856', 'Silver', '243','23','1807','Potassium carbonate os used in glass,while Potassium hydroxide is used in detergent and liquid soap'),
            "Calcium": form('20', 'CA', '40.078', 'Alkaline Earth Metals', '841.9', '1484', '1550', 'Silver', '194','23','1808','aluminum is used as an alloying agent for aluminum,beryllium,copper,lead,and magnesium alloys,and also in building stones for cement'),
            "Scandium": form('21', 'SC', '44.956', 'Transition Metals', '1541', '2830', '2985', 'Silver', '184','24','1879','scandium can be found in high end bicycle frames and baseball hats'),
            "Titanium": form('22', "TI", '47.867', 'Transition Metals', '1668', '3287', '4507', 'Silver', '176','25','1791','titanium alloys are used in spacecraft and missles'),
            "Vanadium": form('23', "V", '50.942', 'Transition Metals', '1910', '3407', '6110', 'Silver', '171','25','1801','vanadium is used in armour plates,axles,tools,piston rods and crankshafts,alloys used in nuclear reactors.'),
            "Chromium": form('24', 'CR', '51.996', 'Transition Metals', '1907', '2671', '7190', 'Silver', '166','25','1797','chromium is used for tanning leather,and manufacturing stainless steel'),
            "Manganese": form('25', "MN", '54.938', 'Transition Metals', '1246', '2061', '7470', 'Silver', '161','25','1774','Manganese\'s main use is in alloys, the most famous being steel,make up about 1.5% of drink cans'),
            "Iron": form('26', "FE", '55.845', 'Transition Metals', '1538', '2861', '7874', 'Gray', '156','27','2000 bce','Iron is used for making reinforced concrete,griders,and manufacturing steel'),
            "Cobalt": form('27', 'Co', '58.933', "Transition Metals", '1495', '2900', '8900', 'Gray', '152','28','1735','cobalt is used in magnets,alloys are used in jet turbines and gas turbine engines'),
            "Nickel": form('28', 'NI', '58.693', 'Transition Metals', '1455', '2913', '8908', 'Gray', '149','30','1751','nickel used in batteries and makes up 25% of the 5 cent coin, the nickel'),
            'Copper': form('29', 'Cu', '63.546', 'Transition Metals', '1084.62', '2562', '8960', 'Copper', '145','28','8000 bce','copper is the main metal in coins and gun metals.'),
            'Zinc': form('30', 'Zn', '65.38', 'Transition Metals', '419.53', '906.9', '7140', 'SlateGray', '142','29','1500','zinc is used to galvanise(coat with zinc) other metals from rusting,while Zinc oxide is used in paints,rubber,cosmetics,plastics,inks,and soaps.'),
            'Gallium': form('31', 'Ga', '69.723', 'Post Transition Metals', '29.760', '2204', '5904', 'Silver', '136','30','1875','Gallium is used in Galinstan-alloy thermometers and Gallium arsenide computer chips'),
            'Germanium': form('32', 'Ge', '72.630', 'Metalloids', '938.25', '2820', '5323', 'Gray', '125','31','1886','Germanium is used in commercial ingot bars, and is also used in dietary supplements.'),
            'Arsenic': form('33', 'As', '74.922', 'Metalloids', '816.9', '614', '5727', 'Silver', '114','32','1250','Arsenic is used in certain poisons and colored fireworks.'),
            'Selenium': form('34', 'Se', '78.971', 'Reactive Nonmetals', '221', '685', '4819', 'Gray', '103','29','1817','Selenium is used as a glaze to give pottery color,and also used in photographer\'s light meters as a photocell.'),
            'Bromine': form('35', 'Br', '79.904', 'Reactive Nonmetals', '-7.350', '58.9', '3120', 'Red', '94','30','1826','Bromine is used in citrus flavored sodas as a brominated vegetable oil, as an emulsifier,and is also used as a tablet to maintain hot tub water'),
            'Krypton': form('36', 'Kr', '83.798', 'Noble Gases', '-157.36', '-153.22', '3.75', 'None', '88','31','1898','Krypton used to be used as a high end lightbulb, before led became the superior choice for light,and is also used as a light, as when electricity passes through it, it glows white-blue.'),
            'Rubidium': form('37', 'Rb', '85.468', 'Alkali Metals', '39.310', '688', '1532', 'Silver', '265','31','1861','Rubidium is sometimes used as a component to photocells,and also used in it’s nitrate form as fireworks for a purple color'),
            'Strontium': form('38', 'Sr', '87.62', 'Alkaline Earth Metals', '776.9', '1382', '2630', 'Silver', '219','32','1790','Strontium is used in fireworks and flares in its salt form, to give them a brilliant color'),
            'Yttrium': form('39', 'Y', '88.906', 'Transition Metals', '1526', '3345', '4472', 'Silver', '212','32','1794','Yttrium is used to increase the strength of aluminum and magnesium alloys, as it is an additive in these alloys, \nit is also used in it\'s oxide form to be added to glass in camera lenses'),
            'Zirconium': form('40', 'Zr', '91.224', 'Transition Metals', '1855', '4409', '6511', 'Silver', '206','32','1789','Zirconium is used in nuclear power stations, as it cannot absorbe neutrons,while its oxide form is used in strong ceramics'),
            'Niobium': form('41', 'Nb', '92.906', 'Transition Metals', '2477', '4744', '8570', 'Gray', '198','32','1801','Niobium alloys are frequently used in certain jet engines and rockets'),
            'Molubdenum': form('42', 'Mo', '95.95', 'Transition Metals', '2623', '4693', '10280', 'Gray', '190','32','1781','Molybdenum is used usally to make alloys,but is also made into grey powder for commercial use.'),
            'Technetium': form('43', 'Tc', '98', 'Transition Metals', '2157', '4265', '11500', 'Silver', '183','33','1937','Technetium is used  for medical diagnostic studies and for protecting steel from corroding,though Technetium is radioactive, so it is hard to use it a lot.','4.12x 106 y'),
            'Ruthenium': form('44', 'Ru', '101.07', 'Transition Metals', '2334', '4150', '12370', 'Silver', '178','33','1844','Ruthenium is frequently used in the electronics industry for chip resistors and electrical contacts,but in its oxide form it can be used in the chemical industry for chlorine production'),
            'Rhodium': form('45', 'Rh', '102.91', 'Transition Metals', '1964', '3695', '12450', 'Silver', '173','33','1803','Rhodium is mostly used in catalytic car converters, and is a very expensive and rare metal.'),
            'Palladium': form('46', 'Pd', '106.42', 'Transition Metals', '1554.90', '2963', '12023', 'Silver', '169','33','1803','Palldium is also used in catalytic car converters, along with rhodium, and is also used in some jewellery.'),
            'Silver': form('47', 'Ag', '107.87', 'Transition Metals', '961.78', '2162', '10490', 'Silver', '165','37','3000 bce','Silver has many uses,such as silverware,mirrors,dental alloys,and batteries.'),
            'Cadmium': form('48', 'Cd', '112.41', 'Transition Metals', '321.07', '766.9', '8650', 'Silver', '161','37','1817','Cadmium is used in rechargeable nickel-cadmium batteries,and it is also used in the rods of nuclear reactors, as it can absorb neutrons.'),
            'Indium': form('49', 'In', '114.82', 'Post Transition Metals', '156.60', '2072', '7310', 'Silver', '156','38','1863','Indium is mostly made in indium tin oxide, which is used a lot and is an important component in touch screens and flatscreen tvs.'),
            'Tin': form('50', 'Sn', '118.71', 'Post Transition Metals', '231.93', '2602', '7310', 'Silver', '145','38','3000 bce','Tin is used in a few different things, such as tin cans and tin foil,which are the most known ones,but it is also used in the process of glass making.'),
            'Antimony': form('51', 'Sb', '121.76', 'Metalloids', '630.63', '1587', '6697', 'Silver', '133','36','3000 bce','Antimony is mostly used to alloy with other metals and improve their stength,such as lead.'),
            'Tellurium': form('52', 'Te', '127.60', 'Metalloids', '449.51', '987.9', '6240', 'Silver', '123','37','1783','Tellurium is mostly made into alloys with copper and stainless steel, and can also be added to lead to improve its hardness'),
            'Iodine': form('53', 'I', '126.90', 'Reactive Nonmetals', '113.7', '184.3', '4940', 'SlateGray', '115','34','1811','Iodine\'s first use was in film camaras,but now it has expanded to many more uses, such as iodine salts and dyes.'),
            'Xenon': form('54', 'Xe', '131.29', 'Noble Gases', '-111.8', '-108', '5.9', 'None', '108','37','1898','Xenon is used in some light sources, as it expelles a powerful glow when an electrical current passes through it, it is also used a propulsion device for certain satelites '),
            'Cesium': form('55', 'Cs', '132.91', 'Alkali Metals', '28.44', '671', '1879', 'Silver', '298','39','1860','Caesium is used primarily as a drilling fluid,but can also be used to make optical glass.'),
            'Barium': form('56', 'Ba', '137.33', 'Alkaline Earth Metals', '730', '1870', '3510', 'Silver', '253','39','1808','Bartium does not have many uses, but 2 of it\'s uses are that it is used in drill fluids and gas wells'),
            'Lanthanum': form('57', 'La', '138.91', 'Lanthanoids', '919.9', '3464', '6146', 'Silver', None, '38','1803','lanthanum is only used commercially in its alloys, such as lanthanum-nickel being used to store hydrogen gas in the gas tanks of hydrogen vechicles, it can also be used as a mischmetal alloys in cigarette lighters.'),
            'Cerium': form('58', 'Ce', '140.12', 'Lanthanoids', '797.9', '3360', '6689', 'Silver', None,'38','1803','Cerium is used in mischmetal alloy,and is used in cigarette lighters, while also being used in its oxide form as an oven cleaner'),
            'Praseodymium': form('59', 'Pr', '140.91', 'Lanthanoids', '930.9', '3290', '6640', 'Silver', '247','38','1885','Praseodymium is mischmetal alloys to create cigarette lighters, and is used as a salt to make colored glass.'),
            'Neodymium': form('60', 'Nd', '144.24', 'Lanthanoids', '1021', '3100', '7010', 'Silver', '206','37','1885','Neodymium is usally used with iron and boron to make powerfull magnets, and is also used in didymium glasses.'),
            'Promethium': form('61', 'Pm', '145', 'Lanthanoids', '1100', '3000', '7264', 'Silver', '205','37','1945','Some promethium is used in atomic batteries,and some of it is used as x-ray measurments.'),
            'Samarium': form('62', 'Sm', '150.36', 'Lanthanoids', '1072', '1803', '7353', 'Silver', '238','37','1879','Samarium is used in certain magnets in combination with cobalt,but these magnets are stronger then the regular iron ones,these magnets are also used in microwave application as they are fairly heat resistant'),
            'Europium': form('63', 'Eu', '151.96', 'Lanthanoids', '821.9', '1500', '5244', 'Silver', '231','37','1901','Europium is used in Euro banknotes,as it was named after the continent of europe,it is also used in low energy lightbulbs'),
            'Gadolinium': form('64', 'Gd', '157.25', 'Lanthanoids', '1313', '3250', '7901', 'Silver', '233','35','1880','Gadolinium is mostly used in alloys,as it can improve iron chromium alloys if added to them, Gadolinium is also used when it is in compounds in mri scans.'),
            'Terbium': form('65', 'Tb', '158.93', 'Lanthanoids', '1356', '3230', '8219', 'Silver', '225','35','1843','Terbium is used in low energy lightbulbs,and mercury lamps'),
            'Dysprosium': form('66', 'Dy', '162.5', 'Lanthanoids', '1412', '2567', '8551', 'Silver', '228','35','1886','Dysprosium is used mainly in neodymium based magnets as an alloy, and these magnets can be used wind turbines and eletrical vechicals'),
            'Holmium': form('67', 'Ho', '164.93', 'Lanthanoids', '1474', '2700', '8795', 'Silver', '226','35','1878','Holmium is used in nuclear reactors,and sometimes its alloys are used in certain magnets'),
            'Erbium': form('68', 'Er', '167.26', 'Lanthanoids', '1497', '2868', '9066', 'Silver', '226','34','1842','Erbium does not have many uses, but it can be used as an oxide in infared absorbing glass,and to give glass a pink tint'),
            'Thulium': form('69', 'Tm', '168.93', 'Lanthanoids', '1545', '1950', '9320', 'Silver', '222','34','1879','Thulium is used in some surgical lasers,and portable x-rays'),
            'Ytterbium': form('70', 'Yb', '173.05', 'Lanthanoids', '818.9', '1196', '6570', 'Silver', '222','33','1878','Ytterbium is starting to be put into memory devices and tuneable lasers,but so far it do not have that many uses other then that.'),
            'Lutetium': form('71', 'Lu', '174.97', 'Lanthanoids', '1663', '3402', '9841', 'Silver', '217','34','1907','Lutetium is barely used,but when it is used it is used to break the hydrocarbons in oil refineries'),
            'Hafnium': form('72  ', 'Hf', '178.49', 'Transition Metals', '2233', '4603', '13310', 'Gray', '208','35','1923','Hafnium is used to make control rods, and is usally alloyed with iron titanium and niobium'),
            'Tantalum': form('73', 'Ta', '180.95', 'Transition Metals', '3017', '5458', '16650', 'Gray', '200','35','1802','Tantalum is mainly used in eletrical parts, and is used to handle corrosive metals'),
            'Tungsten': form('74', 'W', '183.84', 'Transition Metals', '3422', '5555', '19250', 'Gray', '193','34','1783','Tungsten is used to strengthen other metals thorugh alloys,as its melting point is the highest out of all the elements,and tungsten carbon is used a lot in metal working'),
            'Rhenium': form('75', 'Re', '186.21', 'Transition Metals', '3186', '5596', '21020', 'Gray', '188','34','1925','Rhenium is used in alloys with tungsten,and these alloys are mainly used in oven filaments and x-rays'),
            'Osmium': form('76', 'Os', '190.23', 'Transition Metals', '3033', '5012', '22590', 'Bluish-White', '185','34','1803','Osmium is not widely used, but is sometimes used in needles and eletrical contacts'),
            'Iridium': form('77', 'Ir', '192.217', 'Transition Metals', '2466', '4428', '22560', 'Silvery-White','180','35','1803','Iridium is used mostly to alloy with osmium,this alloys they make is used in pen tips and compass bearings'),
            'Platium': form('78', 'Pt', '195.084', 'Transition Metals', '1768.3', '3825', '21450', 'Silverish-White','177','36','1735','Platinum is used in jewelery,but it is also used in catalytic converters along with rhodium and palldium'),
            'Gold': form('79', 'Au', '196.977', 'Transition Metals', '1064.18', '2856', '19300', 'Yellow', '174','36','2500 bce','Gold is sometimes used in golden jewelery,and also in some coins'),
            'Mercury': form('80', 'Hg', '200.59', 'Transition Metals', '-38.83', '356.73', '13534', 'Silver', '171','39','1500 bce','Since mercury is very toxic,it does not have much use, but it is rarely used in eletrical switchs and rectifiers'),
            'Thallium': form('81', 'TI', '204.38', 'Post Transition Metals', '304', '1473', '11850', 'Gray', '156','38','1861','Thallium sulfate used to be an effective rodent killer, but most places have banned it for its toxic properties,Thallium is used in some photoeletric cells.'),
            'Lead': form('82', 'Pb', '207.2', 'Post Transition Metals', '327.46', '1749', '11340','Silver-Hint of Blue', '154','37','4000 bce','Lead is a very common metal,so common that we use it to write,and lead has other uses too,such as car batteries.'),
            'Bismuth': form('83', 'Bi', '208.980', 'Post Transition Metals', '271.3', '1564', '9780', 'Silvery-White','143','38','1400','Bismuth is mainly used in alloys with tin or cadmium,this alloy is primarily used in fire detectors and extinguishers','1.9x1019 y'),
            'Polonium': form('84', 'Po', '209', 'Post Transition Metals', '255', '961.9', '9196', 'Silver', '135','32','1898','Polonium is usally used in antistatic devices,as Polonium is aplha-emitter','102.1 y'),
            'Astatine': form('85', 'At', '210', 'Metalloids', '302', '350', 'None', 'Silver', '127','30','1940','Astatine has no uses, as its half life is only 8 hours','8.06h'),
            'Radon': form('86', 'Rn', '222', 'Noble Gases', '-71.1', '-68.85', '9.73', 'Colorless ', '120','33','1900','Radon is used in cancer therapy as it is radioactive,and it can also be used to treat tumors','3.823495 d'),
            'Francium': form('87', 'Fr', '223', 'Alkali Metals', '20.9', '650', 'None', 'Silver-Gray-Metallic','None','1939','33','Francium in its most stable isoptope only lasts for 22 minutes, so it has no uses','21.7 m'),
            'Radium': form('88', 'Ra', '226', 'Alkaline Earth Metals', '700', '1737', '5000', 'Silver-WHite', 'None','32','1898','Radium is barely used as it is radioactive, but it is used to treat prostate cancer','1.59x103 y'),
            'Actinium': form('89', 'Ac', '227', 'Actinoids', '1050', '3200', '10070', 'Silver-White', 'None','30','1899','Actinium is barely used outside of research,as it is very radioactive','21.7865 y'),
            'Thorium': form('90', 'Th', '232.038', 'Actinoids', '1750', '4820', '11724', 'Silver', 'None','29','1829','Thorium is used in magnesium alloys to give it more strength,and thorium oxide can be used as an industrial catalyst','1.406x1010y'),
            'Protactinium': form('91', 'Pa', '231.036', 'Actinoids', '1572', '4000', '15370', 'Silver-Gray', 'None','1913','28','Protractium has no uses outside of research','32788y'),
            'Uranium': form('92', 'U', '238.029', 'Actinoids', '1135', '3900', '19050', 'Silver-Gray', 'None','26','1789','Uranium is the element that gives us nuclear fuel, and is used in nuclear subs and weapons','4.471x109y'),
    }

window = tk.Tk()
window.title('The Periodic Database')
label = tk.Label(text="What Element do you want to look at?")
label.pack()
Elementneeded = tk.Entry(width=50)
Elementneeded.pack()
Text_box = tk.Text(height='50',width='100')
Text_box.pack()

def Clearbox():
    Text_box.delete('1.0','end')
    Elementneeded.delete(0,'end')
    Stringvar.set('None')
Num = 0
def Next(self):
    global Num
    global Stringvar
    try:
        Num = list(Elements).index(Elementneeded.get())
        if Num == length:
                Num = 0
                Index = list(Elements.keys())[Num]
                Elementneeded.delete(0,'end')
                Elementneeded.insert(0,Index)
                Newindex = Elements[Index]
                Text_box.delete('1.0','end')
                Text_box.insert('1.0',Newindex)
                Stringvar.set(Elementneeded.get())
        else:
                Num = Num + 1
                Index = list(Elements.keys())[Num]
                Elementneeded.delete(0,'end')
                Elementneeded.insert(0,Index)
                Newindex = Elements[Index]
                Text_box.delete('1.0','end')
                Text_box.insert('1.0',Newindex)
                Stringvar.set(Elementneeded.get())
    except:
         Text_box.delete('1.0','end')
         Text_box.insert('1.0','You can not move through elements if no valid element is selected')


def Back(self):
    global Stringvar
    global Num

    try:
        Num = list(Elements).index(Elementneeded.get())
        if Num == 0:
                Num = length
                Index = list(Elements.keys())[Num]
                Elementneeded.delete(0,'end')
                Elementneeded.insert(0,Index)
                Newindex = Elements[Index]
                Text_box.delete('1.0','end')
                Text_box.insert('1.0',Newindex)
                Stringvar.set(Elementneeded.get())
        else:
            
                Num = Num - 1
                Index = list(Elements.keys())[Num]
                Elementneeded.delete(0,'end')
                Elementneeded.insert(0,Index)
                Newindex = Elements[Index]
                Text_box.delete('1.0','end')
                Text_box.insert('1.0',Newindex)
                Stringvar.set(Elementneeded.get())
    except:
         Text_box.delete('1.0','end')
         Text_box.insert('1.0','You can not move through elements if no valid element is selected')
lis = []
for x in range(0,length):
    i = list(Elements.keys())[x]
    lis.append(i)

def callback(selection):
    Text_box.delete('1.0','end')
    Text_box.insert('1.0',Elements[selection])
    Elementneeded.delete(0,'end')
    Elementneeded.insert(0,selection)
def Search(self):
    global Stringvar
    Text_box.delete('1.0','end')
    try:
        Text_box.insert('1.0',Elements[Elementneeded.get()])
        Stringvar.set(Elementneeded.get())
    except:
        Text_box.insert('1.0','That is not an element')

Stringvar = tk.StringVar(window,'None')

Dropdown = tk.OptionMenu(window,Stringvar,*lis,command=callback)
Dropdown.pack()
def scale(value):
    Text_box.config(width=value)
Clear = tk.Button(text="Clear",command=Clearbox)
Clear.pack()

boxscale = tk.Scale(window,from_=100,to=200,command=scale,orient='horizontal',label='Text Box Width')
boxscale.pack()
window.bind('<Return>',Search)
window.bind('<Right>',Next)
window.bind('<Left>',Back)

window.mainloop()
#Binds






