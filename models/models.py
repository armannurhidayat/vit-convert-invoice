# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class Import(models.Model):
    _name = 'convert_invoice.convert_invoice'

    name = fields.Char(
        string='Nama Debitur',
        required=True,
    )
    peminjam = fields.Char(
        string='Nama Peminjam',
    )
    bunga_peminjam = fields.Char(
        string='Bunga Peminjam Pertahun',
    )
    jangka_waktu = fields.Char(
        string='Jangka Waktu Pinjaman (Bulan)',
    )
    tgl_pencairan = fields.Date(
        string='Tanggal Pencairan',
        default=lambda self: time.strftime("%Y-%m-%d")
    )
    priode_pinjaman = fields.Date(
        string='Priode Pinjaman',
        default=lambda self: time.strftime("%Y-%m-%d")
    )
    mulai_pembayaran = fields.Integer(
        string='Mulai Pembayaran Pinjaman (Bulan)',
    )
    bulan = fields.Integer(
        string='Bulan',
    )
    periode = fields.Date(
        string='Periode'
    )
    saldo_awal = fields.Float(
        string='Saldo Awal',
    )
    pokok = fields.Float(
        string='Pokok',
    )
    bunga = fields.Float(
        string='Bunga',
    )
    saldo_akhir = fields.Float(
        string='Saldo Akhir',
    )
    status = fields.Char(
        string='Status',
    )
    tanggal = fields.Date(
        string='Tanggal',
        default=lambda self: time.strftime("%Y-%m-%d")
    )
    is_invoice = fields.Boolean(
        string='Is Invoice',
    )

    @api.model
    def convert_invoice(self, values):
        # Mengambil Object
        object_convert = self.env['convert_invoice.convert_invoice']
        object_invoice = self.env['account.invoice']
        object_partner = self.env['res.partner']
        object_account = self.env['account.account']
        object_product = self.env['product.product']

        # Search record pada object
        records = object_convert.search([('status', '=', 'OPEN'), ('is_invoice', '=', False)])  # kondisi search

        for record in records:
            partner_id = object_partner.search([('name', '=', record.name)])
            account_id = object_account.search([('code', '=', '101200')])
            product_id = object_product.search([('name', '=', 'PokokCicilan')])


            date_invoice = record.periode

            invoice_line_ids = [(0, 0, {
                'product_id': product_id.id,  # product_id dari variabel search object
                'name': 'cicilan',
                'quantity': 1,
                'price_unit': record.pokok,
                'account_id': account_id.id,
            })]

            data = {
                'partner_id'      : partner_id.id,
                'date_invoice'    : record.periode,
                'invoice_line_ids': invoice_line_ids,
            }
            object_invoice.create(data)
            record.is_invoice=True