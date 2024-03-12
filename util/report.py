try:
    import util.frozen as frozen
except:
    import qt0922.util.frozen as frozen


class MyReport():
    def __init__(self):
        self.html_content = '<!doctype html>\
                            <html>\
                            <head>\
                            <meta charset="utf-8">\
                            </head>\
                            <h1 align="center" style="font-size:20px;font-family:fangsong;">过敏原检验报告单</h1>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>姓名：%s</td>\
                                    <td>性别：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本号：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>条码号：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本类型：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>测试时间：%s</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>过敏原</td>\
                                    <td>结果</td>\
                                    <td>参考值</td>\
                                    <td>结果解释</td>\
                                </tr>\
                                %s\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>注</td>\
                                </tr>\
                                <tr>\
                                    <td>“-”为阴性，＜0.35IU/mL</td>\
                                </tr>\
                                <tr>\
                                    <td>“+”为弱性，0.35IU/mL-3.5IU/mL</td>\
                                </tr>\
                                <tr>\
                                    <td>“++”为中性，3.5IU/mL-17.5IU/mL</td>\
                                <tr>\
                                    <td>“+++”为强阳，≥17.5IU/mL</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>打印时间：%s</td>\
                                </tr>\
                                <tr>\
                                    <td>此检验报告只对此标本负责，请结合临床。</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <body>\
                            </body>\
                            </html>\
                            '
        
    def gethtml(self, item_type, reagent_info, nature_aver_str):
        # < 60000: "阴性" "-"
        # < 660000: "弱阳性" "+"
        # < 1100000: "中阳性" "++"
        # > 1100000: "强阳性" "+++"
        result_dict = {"阴性": "-", "中阳性": "++", "强阳性": "+++", "弱阳性": "+"}
        # + —计算列表 40
        result_list_1 = [result_dict.get(i) for i in nature_aver_str.split(",")[5:]]
        # 阴阳性计算列表 40
        result_list_2 = [i for i in nature_aver_str.split(",")[5:]]
        reagent_info_list_1 = [i for i in reagent_info.split(",")]
        reagent_info_list_2 = [reagent_info_list_1[k:k+5] for k in [j for j in range(0, 55, 5)] if k % 15 == 0]
        # 过敏原列表
        reagent_info_list_3 = [i for i in sum(reagent_info_list_2, []) if i != '']

        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        # + —结果列表
        result_list_3 = [result_list_1[i] for i in range(len(allergen)) if allergen[i] != ""]
        # 阴阳性结果列表
        result_list_4 = [result_list_2[i] for i in range(len(allergen)) if allergen[i] != ""]
        # 姓名，性别，样本号，条码号，样本类型，测试时间，【结果】，打印时间
        temp = '<tr align="center">\
                <td>%s</td>\
                <td>%s</td>\
                <td>&lt;0.35</td>\
                <td>%s</td>\
                </tr>'
        temp_str = "".join([temp % (str(j + 1) + reagent_info_list_3[j], result_list_3[j], result_list_4[j]) for j in range(len(reagent_info_list_3))])
        # for j in range(len(reagent_info_list_3)):
        #     str_temp = temp
        #     temp_str = temp_str + str_temp % (str(j + 1) + reagent_info_list_3[j], result_list_3[j], result_list_4[j])
        return self.html_content, temp_str