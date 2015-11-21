'''Generates the list of country codes, grabs the corresponding data from the 
web and prints the table of women's average first marriage age for each country.'''

import pandas as pd
import os
from Quandl import Quandl
import time
import requests
import json

auth_token = 'eVv_a2tQw8n-vmEVbcam' # Personal authentication token for Kelsey's account, replace if needed

'''
Countries listed in Quandl dataset of women's age at first marriage are:
1. Afghanistan
2. Albania
3. Algeria
4. Angola
5. Antigua and Barbuda
6. Argentina
7. Armenia
8. Australia
9. Austria
10. Azerbaijan
11. Bahrain
12. Bangladesh
13. Barbados
14. Belarus
15. Belgium
16. Belize
17. Benin
18. Bhutan
19. Bolivia
20. Bosnia and Herzegovina
21. Botswana
22. Brazil
23. Brunei
24. Bulgaria
25. Burkina Faso
26. Burundi
27. Cambodia
28. Cameroon
29. Canada
30. Cape Verde
31. Central African Republic
32. Chad
33. Chile
34. China
35. Colombia
36. Comoros
37. Congo
38. Congo-Brazzaville
39. Costa Rica
40. Croatia
41. Cuba
42. Cyprus
43. Czech Republic
44. Denmark
45. Dominica
46. Dominican Republic
47. Ecuador
48. Egypt
49. El Salvador
50. Equatorial Guinea
51. Eritrea
52. Estonia
53. Ethiopia
54. Fiji
55. Finland
56. France
57. Gabon
58. Gambia
59. Georgia
60. Germany
61. Ghana
62. Greece
63. Grenada
64. Guatemala
65. Guinea
66. Guinea-Bissau
67. Guyana
68. Haiti
69. Honduras
70. Hong Kong
71. Hungary
72. Iceland
73. India
74. Indonesia
75. Iran
76. Iraq
77. Ireland
78. Israel
79. Italy
80. Ivory Coast
81. Jamaica
82. Japan
83. Jordan
84. Kazakhstan
85. Kenya
86. Kiribati
87. Kosovo
88. Kuwait
89. Kyrgyzstan
90. Laos
91. Latvia
92. Lebanon
93. Lesotho
94. Liberia
95. Libya
96. Lithuania
97. Luxembourg
98. Macedonia
99. Madagascar
100. Malawi
101. Malaysia
102. Maldives
103. Mali
104. Mauritania
105. Mauritius
106. Mexico
107. Moldova
108. Mongolia
109. Montenegro
110. Morocco
111. Mozambique
112. Myanmar
113. Namibia
114. Nepal
115. Netherlands
116. New Zealand
117. Nicaragua
118. Niger
119. Nigeria
120. North Korea
121. Norway
122. Oman
123. Pakistan
124. Panama
125. Papua New Guinea
126. Paraguay
127. Peru
128. Philippines
129. Poland
130. Portugal
131. Qatar
132. Romania
133. Russia
134. Rwanda
135. Saint Kitts and Nevis
136. Saint Lucia
137. Saint Vincent and the Grenadines
138. Samoa
139. San Marino
140. Sao Tome and Principe
141. Saudi Arabia
142. Senegal
143. Serbia
144. Seychelles
145. Sierra Leone
146. Singapore
147. Slovak Republic
148. Slovenia
149. Solomon Islands
150. Somalia
151. South Africa
152. South Korea
153. South Sudan
154. Spain
155. Sri Lanka
156. Sudan
157. Suriname
158. Swaziland
159. Sweden
160. Switzerland
161. Syria
162. Tajikistan
163. Tanzania
164. Thailand
165. The Bahamas
166. Timor-Leste
167. Togo
168. Tonga
169. Trinidad and Tobago
170. Tunisia
171. Turkey
172. Turkmenistan
173. Tuvalu
174. UAE
175. Uganda
176. UK
177. Ukraine
178. Uruguay
179. USA
180. Uzbekistan
181. Vanuatu
182. Venezuela
183. Vietnam
184. Yemen
185. Zambia
186. Zimbabwe
'''

country_keys = []

def form_dictionary():
    r = requests.get('http://s3.amazonaws.com/quandl-static-content/World+Bank+Descriptions/country_codes')
    country_codes = r.text

    country_codes_split = country_codes.splitlines()
    country_array = []

    for a in country_codes_split:
        if a != '' and a != 'COUNTRY|CODE': # removing heading and blank lines
            l = a.split('|')
            m = [l[1], l[0]]
            country_array.append(m)

    x = dict(country_array)
    return x

for key in form_dictionary():
    data_string = 'WORLDBANK/' + key + '_SP_DYN_SMAM_FE' # format of the data on Quandl database
    country_keys.append(data_string)

'''
# Test data - Afghanistan, Albania, Algeria, Antigua and Barbada, Argentina, USA, Channel Islands (Channel Islands not in database)
test_country_keys = ['WORLDBANK/AFG_SP_DYN_SMAM_FE', 'WORLDBANK/ALB_SP_DYN_SMAM_FE', 'WORLDBANK/DZA_SP_DYN_SMAM_FE', 'WORLDBANK/ATG_SP_DYN_SMAM_FE', 'WORLDBANK/ARG_SP_DYN_SMAM_FE', 'WORLDBANK/USA_SP_DYN_SMAM_FE', 'WORLDBANK/CHI_SP_DYN_SMAM_FE']
firstmarriage = Quandl.get(test_country_keys, authtoken=auth_token, order='desc')
'''

firstmarriage = Quandl.get(country_keys, authtoken=auth_token, order='desc')

firstmarriage_trimmed = {} # type is dict, no longer pandas DataFrame - DataFrame doesn't allow me to strip out null values, must be even matrix
for key in firstmarriage:
    if key[-9:] == 'NOT FOUND': # skipping the countries we have no data for
        continue
    trimmed_data = firstmarriage[key].dropna() # removes the null values from the series
    country_longform = key[10:13]
    trimmed_data.name = form_dictionary()[country_longform] # Name attribute is now human readable country, note that name goes below corresponding data
    firstmarriage_trimmed[key] = trimmed_data # forming a new dict with the trimmed series

f = open('marriage', 'w')
f.write(str(firstmarriage_trimmed))
f.close()

# TODO: Remove extraneous Name, dtype entries from the dataset